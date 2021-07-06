#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/7/6
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
from ._cursor import Cursor


class Connection:
    def cursor(self, *args, **kwargs) -> Cursor:
        pass

    def close(self) -> None:
        pass
