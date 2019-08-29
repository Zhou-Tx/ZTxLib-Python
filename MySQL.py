#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from pymysql import connect


class MySQL:
    def __init__(self,
                host='127.0.0.1',           # 要连接的主机地址
                port=3306,                  # 端口
                user='root',                # 用于登录的数据库用户
                password=None,              # 密码
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

    def Fetchone(self, sql:str, args=None) -> 'Fetch the first record from the database with the sql sentence':
        db = self.__dbConnect()
        cursor = db.cursor()
        try:
            cursor.execute(sql, args)
            return cursor.fetchone()
        except:
            db.rollback()
            return None
        finally:
            db.close()

    def Fetchall(self, sql:str, args=None) -> 'Fetch all records from the database with the sql sentence':
        db = self.__dbConnect()
        cursor = db.cursor()
        try:
            cursor.execute(sql, args)
            return cursor.fetchall()
        except:
            db.rollback()
            return None
        finally:
            db.close()

    def ExecuteNonQuery(self, sql:str, args=None) -> 'Execute a sql sentence to the database':
        db = self.__dbConnect()
        cursor = db.cursor()
        try:
            cursor.execute(sql, args)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            return False
        finally:
            db.close()

    def ExecuteTrans(self, sql:list) -> 'Execute a transaction to the database with a list of sql sentence':
        db = self.__dbConnect()
        cursor = db.cursor()
        try:
            for query_args in sql:
                query = None
                args = None
                if type(query_args) == str:
                    query = query_args
                elif type(query_args) == tuple:
                    query = query_args[0]
                    if len(query_args) == 2:
                        args = query_args[1]
                    elif len(query_args) != 1:
                        raise Exception()
                else:
                    raise Exception()
                cursor.execute(query, args)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            return False
        finally:
            db.close()
