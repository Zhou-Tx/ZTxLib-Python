#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/7/6
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
from ._connection import Connection
from ._cursor import Cursor


class MariaDBContextManager:
    def __init__(self, pool):
        self.pool = pool

    def __enter__(self) -> Cursor:
        self.connection: Connection = self.pool.get_connection()
        self.cursor: Cursor = self.connection.cursor(named_tuple=True)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()
