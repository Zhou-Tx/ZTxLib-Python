#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2020/12/24 0024
# @Author   :  ZhouTianxing
# @Software :  PyCharm x64
""""""
import mariadb

from .MariaDBContextManager import MariaDBContextManager
from ._connection import Connection


class MariaDB(mariadb.ConnectionPool):
    def __init__(
            self,
            name: str = 'pool',  # 连接池名称
            host: str = 'localhost',  # 数据库地址
            port: int = 3306,  # 数据库端口
            user: str = 'root',  # 用户名
            password: str = '',  # 密码
            database: str = '',  # 数据库名称
            autocommit: bool = True,
    ):
        super().__init__(
            pool_name=name,
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            autocommit=autocommit,
        )
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.autocommit = autocommit

    def __repr__(self):
        return "MariadbConnectionPool<host=%s,port=%d,database=%s>" % (self.host, self.port, self.database)

    def get_connection(self, *args, **kwargs) -> Connection:
        try:
            connection = super().get_connection(*args, **kwargs)
            return connection
        except mariadb.PoolError:
            connection = mariadb.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                autocommit=self.autocommit,
            )
            try:
                self.add_connection(connection)
            except mariadb.PoolError:
                pass
            return connection

    def start(self) -> MariaDBContextManager:
        return MariaDBContextManager(self)
