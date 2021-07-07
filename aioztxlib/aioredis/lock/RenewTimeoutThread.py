#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/7/7
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
import asyncio
import time
from threading import Thread


class RenewTimeoutThread(Thread):
    def __init__(self, renew) -> None:
        super().__init__()
        self._renew = renew
        self._running = False

    def start(self) -> None:
        self._running = True
        super().start()

    def run(self) -> None:
        while self._running:
            asyncio.run(self._renew(30))
            time.sleep(10)

    def stop(self) -> None:
        self._running = False
