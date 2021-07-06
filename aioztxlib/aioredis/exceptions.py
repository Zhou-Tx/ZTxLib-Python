#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/7/6
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
from aioredis import RedisError


class RedisTimeoutError(RedisError, TimeoutError):
    pass


class UnlockError(RedisError):
    pass
