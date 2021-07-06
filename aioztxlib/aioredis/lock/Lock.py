#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/7/6
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
import asyncio
import logging
import time
import uuid
from logging import Logger
from threading import Thread

from aioredis import ConnectionsPool

from . import ScriptingSha
from .ScriptingCommandsMixin import ScriptingCommandsMixin
from ..exceptions import RedisTimeoutError, UnlockError


class Lock:
    logger: Logger = logging.getLogger("RedisLock")

    def __init__(self, pool: ConnectionsPool):
        self.pool = pool
        self.name = None
        self.uuid = None
        self.renew_timeout = None
        self.scripting = ScriptingCommandsMixin(pool)

    async def acquire(self,
                      name: str,
                      wait_timeout: int = 0,
                      timeout: int = 0
                      ):
        await ScriptingSha.initialize(script_load=self.scripting.script_load)
        self.name = "lock:%s" % name
        self.uuid = str(uuid.uuid4())
        start_time = time.time()
        while True:
            if timeout:
                if await self._acquire(timeout):
                    Lock.logger.info("Acquired RedisLock [%s]", self.name)
                    return True
            else:
                if await self._acquire(30):
                    self.renew_timeout = dict(
                        thread=Thread(target=self._renew_timeout),
                        renewing=True,
                    )
                    self.renew_timeout['thread'].start()
                    Lock.logger.info("Acquired RedisLock [%s]", self.name)
                    return True
            if wait_timeout and time.time() - start_time > wait_timeout:
                raise RedisTimeoutError("Timeout while waiting for [%s]" % self.name)
            await asyncio.sleep(0.01)

    async def release(self):
        if await self.scripting.eval_sha(
                ScriptingSha.RELEASE,
                keys=[self.name],
                args=[self.uuid]
        ):
            self.renew_timeout.update(renewing=False)
            Lock.logger.info("Released RedisLock [%s]", self.name)
            return True
        raise UnlockError

    async def extend(self, timeout: int):
        await self.scripting.eval_sha(
            ScriptingSha.EXTEND,
            keys=[self.name],
            args=[self.uuid, timeout * 1000]
        )

    async def renew(self, timeout: int):
        await self.scripting.eval_sha(
            ScriptingSha.RENEW,
            keys=[self.name],
            args=[self.uuid, timeout * 1000]
        )

    async def _acquire(self, timeout: int):
        return await self.scripting.eval_sha(
            ScriptingSha.ACQUIRE,
            keys=[self.name],
            args=[self.uuid, timeout * 1000]
        )

    def _renew_timeout(self):
        while self.renew_timeout['renewing']:
            asyncio.run(self.renew(30))
            time.sleep(20)
