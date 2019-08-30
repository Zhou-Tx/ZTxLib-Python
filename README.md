# ZTxLib
# 简体中文

目录
1.MyHTML.py
2.MySQL.py
3.MyThread.py

1.MyHTML.py  # MyHTML类
from MyHTML import MyHTML
构造函数：
MyHTML(url)
该类用于获得url的相关信息，包括：
Host:主机名
IP:IP地址
Response:Request返回的响应信息
BeautifulSoup:BeautifulSoup对象，可用于查找结点
HTML:完整的html源码
Text:无标签纯文本

2.MySQL.py  # MySQL类
from MySQL import MySQL
构造函数：
MySQL(
    host='127.0.0.1',       # 要连接的主机地址
    port=3306,              # 端口
    user='root',            # 用于登录的数据库用户
    password='root',        # 密码
    database=None,          # 要连接的数据库
    passwd=None,            # 同 password，为了兼容 MySQLdb
    db=None,                # 同 database，为了兼容 MySQLdb
    charset='utf8',         # 字符编码
    connect_timeout=10      # 连接超时时间，(1-31536000)
)
该类用于对MySQL数据库进行操作，包括：
Fetchone(sql,args)          # 根据sql语句从数据库中查询一条记录
Fetchall(sql,args)          # 根据sql语句从数据库中查询全部记录
ExecuteNonQuery(sql,args)   # 向数据库提交一条sql语句
ExecuteTrans(sqlList)       # 建立一个事务，提交sql语句列表

3.MyThread.py  # MyThread类
from MyThread import MyThread
构造函数：
MyThread(method)
该类用于以多线程方式执行函数体，操作方法
start()                     # 执行构造的无参方法
start(args)                 # 执行构造的有参方法，参数随该函数传递
wait()                      # 等待多线程方法执行完毕（阻塞进程）

...未完，待续...
