#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2019/12/26
# @Author   :  ZhouTianxing
# @Software :  PyCharm Professional x64
# @FileName :  _sqlite
""""""
from sqlite3 import connect, DatabaseError


class SQLite:
    def __init__(self,
                 database,
                 timeout=None,
                 detect_types=None,
                 isolation_level=None,
                 check_same_thread=None,
                 factory=None,
                 cached_statements=None,
                 uri=None):
        """
        connect(
            database[, timeout, detect_types, isolation_level,
            check_same_thread, factory, cached_statements, uri]
        )
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
        if self.__timeout is None:
            return connect(self.__database)
        elif self.__detect_types is None:
            return connect(self.__database,
                           self.__timeout)
        elif self.__isolation_level is None:
            return connect(self.__database,
                           self.__timeout,
                           self.__detect_types
                           )
        elif self.__check_same_thread is None:
            return connect(self.__database,
                           self.__timeout,
                           self.__detect_types,
                           self.__isolation_level
                           )
        elif self.__factory is None:
            return connect(self.__database,
                           self.__timeout,
                           self.__detect_types,
                           self.__isolation_level,
                           self.__check_same_thread
                           )
        elif self.__cached_statements is None:
            return connect(self.__database,
                           self.__timeout,
                           self.__detect_types,
                           self.__isolation_level,
                           self.__check_same_thread,
                           self.__factory
                           )
        elif self.__uri is None:
            return connect(self.__database,
                           self.__timeout,
                           self.__detect_types,
                           self.__isolation_level,
                           self.__check_same_thread,
                           self.__factory,
                           self.__cached_statements
                           )
        else:
            return connect(self.__database,
                           self.__timeout,
                           self.__detect_types,
                           self.__isolation_level,
                           self.__check_same_thread,
                           self.__factory,
                           self.__cached_statements
                           )

    def fetchone(self, sql: str, args=None) -> tuple or None:
        """
        Fetch the first record matches the sql sentence
        :param sql:a querying sql sentence
        :param args:a object, a tuple or a dict with the committing arguments or None
        :return:a tuple of a record
        """
        db = self.__connect()
        cursor = db.cursor()
        try:
            if args is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, args)
            return cursor.fetchone()
        except DatabaseError:
            db.rollback()
            return None
        finally:
            db.close()

    def fetchall(self, sql: str, args=None) -> tuple or None:
        """
        Fetch all the records match the sql sentence
        :param sql:a querying sql sentence
        :param args:a object, a tuple or a dict with the committing arguments or None
        :return:a list of all the records
        """
        db = self.__connect()
        cursor = db.cursor()
        try:
            if args is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, args)
            return cursor.fetchall()
        except DatabaseError:
            db.rollback()
            return None
        finally:
            db.close()

    def update(self, sql: str, args=None) -> int:
        """
        commit a sql sentence to modify the database
        :param sql:an updating sql sentence
        :param args:a object, a tuple or a dict with the committing arguments or None
        :return:the count of changed records
        """
        return self.update_batch_((sql, args))

    def update_batch(self, args: list) -> int:
        """
        commit some sql sentences to modify the database
        :param args: a list contains several tuple of sql and args,
            such as [(sql1,args1),(sql2,args2),...] where args may be a object, a tuple, a dict or None
        :return:
        """
        return self.update_batch_(*args)

    def update_batch_(self, *args) -> int:
        """
        commit some sql sentences to modify the database
        :param args: a list contains several tuple of sql and args,
            such as [(sql1,args1),(sql2,args2),...] where args may be a object, a tuple, a dict or None
        :return:
        """
        db = self.__connect()
        cursor = db.cursor()
        try:
            cnt = 0
            for sql in args:
                if len(sql) == 2 and sql[1] is None:
                    cnt += (cursor.execute(sql[0]) is not None)
                else:
                    cnt += (cursor.execute(sql[0], sql[1]) is not None)
            db.commit()
            return cnt
        except DatabaseError as e:
            print(e)
            db.rollback()
            return 0
        finally:
            db.close()
