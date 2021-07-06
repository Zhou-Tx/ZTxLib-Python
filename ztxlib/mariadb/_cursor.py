#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/7/6
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
from typing import Any


class Cursor:
    def execute(self, statement: str, data: Any = None) -> None:
        pass

    def executemany(self, statement: str, data: list[Any] = None) -> None:
        pass

    def fetchone(self) -> Any:
        pass

    def fetchall(self) -> list[Any]:
        pass

    def close(self) -> None:
        pass
