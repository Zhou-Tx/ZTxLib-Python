#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2019/12/26
# @Author   :  Zhou Tianxing
# @Software :  PyCharm Professional x64
# @FileName :  _sqlite
""""""
from sqlite3 import connect


# TODO


class SQLite:
    def __init__(self,
                 database,
                 timeout=None,
                 detect_types=None,
                 isolation_level=None,
                 check_same_thread=None,
                 factory=None,
                 cached_statements=None,
                 uri=None
                 ):
        """
        connect(database[, timeout, detect_types, isolation_level,
            check_same_thread, factory, cached_statements, uri])
        """
        self.__database = database
        self.__timeout = timeout
        self.__detect_types = detect_types
        self.__isolation_level = isolation_level
        self.__check_same_thread = check_same_thread
        self.__factory = factory
        self.__cached_statements = cached_statements
        self.__uri = uri

    def __connect(self) -> connect:
        return connect(
            database=self.__database,
            timeout=self.__timeout,
            detect_types=self.__detect_types,
            isolation_level=self.__isolation_level,
            check_same_thread=self.__check_same_thread,
            factory=self.__factory,
            cached_statements=self.__cached_statements,
            uri=self.__uri
        )

