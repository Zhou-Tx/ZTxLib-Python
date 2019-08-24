from pymysql import connect

class MySQL:
    def __init__(self,
                host='127.0.0.1',               # 要连接的主机地址
                port=3306,                      # 端口
                user='root',                    # 用于登录的数据库用户
                password=None,                  # 密码
                database=None,                  # 要连接的数据库
                passwd=None,                    # 同 password，为了兼容 MySQLdb
                db=None,                        # 同 database，为了兼容 MySQLdb
                charset='utf8',                 # 字符编码
                connect_timeout=10              # 连接超时时间，(1-31536000)
            ):
        self.__host__=host
        self.__user__=user
        self.__password__=password
        self.__database__=database
        self.__port__=port
        self.__charset__=charset
        self.__connect_timeout__=connect_timeout
        self.__db__=db
        self.__passwd__=passwd

    # 私有函数，连接数据库
    def __dbConnect__(self):
        return connect(
            host=self.__host__,
            user=self.__user__,
            password=self.__password__,
            database=self.__database__,
            port=self.__port__,
            charset=self.__charset__,
            connect_timeout=self.__connect_timeout__,
            db=self.__db__,
            passwd=self.__passwd__
        )

    # 公有函数，向数据库提交SQL语句并执行，可用于INSERT,DELETE,UPDATE,TRUNCATE等
    def Commit(self, sql):
        db = self.__dbConnect__()
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

    # 公有函数，执行SQL语句查询，返回一条结果，可用于SELECT
    def Fetchone(self, sql):
        db = self.__dbConnect__()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchone()
        except:
            db.rollback()
            return None
        finally:
            db.close()

    # 公有函数，执行SQL语句查询，返回全部结果，可用于SELECT
    def Fetchall(self, sql):
        db = self.__dbConnect__()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            db.rollback()
            return None
        finally:
            db.close()


# 演示
if __name__ == "__main__":
    db = MySQL(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="root",
        db="websites",
        charset="utf8",
        connect_timeout=5
    )
    db.Commit("UPDATE `link_config` SET state=0 WHERE state=0")
    print(db.Fetchone("SELECT * FROM `link_config` WHERE state=0"))
    print(db.Fetchall("SELECT * FROM `link_config` WHERE state=1"))

