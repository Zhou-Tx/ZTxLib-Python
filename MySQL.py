#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pymysql import connect


class MySQL:
    def __init__(self,
                host='127.0.0.1',           # 要连接的主机地址
                port=3306,                  # 端口
                user='root',                # 用于登录的数据库用户
                password='root',            # 密码
                database=None,              # 要连接的数据库
                passwd=None,                # 同 password，为了兼容 MySQLdb
                db=None,                    # 同 database，为了兼容 MySQLdb
                charset='utf8',             # 字符编码
                connect_timeout=10          # 连接超时时间，(1-31536000)
            ):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.__port = port
        self.__charset = charset
        self.__connect_timeout = connect_timeout
        self.__db = db
        self.__passwd = passwd

    # Private, connect to the mysql database server
    def __dbConnect(self):
        return connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database,
            port=self.__port,
            charset=self.__charset,
            connect_timeout=self.__connect_timeout,
            db=self.__db,
            passwd=self.__passwd
        )

    def Fetchone(self, sql) -> 'Fetch the first record from the database with the sql sentence':
        db = self.__dbConnect()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchone()
        except:
            db.rollback()
            return None
        finally:
            db.close()

    def Fetchall(self, sql) -> 'Fetch all records from the database with the sql sentence':
        db = self.__dbConnect()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            db.rollback()
            return None
        finally:
            db.close()

    def Execute(self, sql) -> 'Execute a sql sentence to the database':
        db = self.__dbConnect()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            return False
        finally:
            db.close()

    def ExecuteAll(self, sqlList) -> 'Execute a transaction to the database with a list of sql sentences':
        db = self.__dbConnect()
        cursor = db.cursor()
        try:
            for sql in sqlList:
                cursor.execute(sql)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            return False
        finally:
            db.close()
