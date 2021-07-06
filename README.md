# ZTxLib

## Copyright ©Zhou Tianxing

### 一、目录

* [一、目录](#一目录)
* [二、项目结构](#二项目结构)
* [三、使用说明](#三使用说明)
  * [1、ztxlib](#1ztxlib)
  * [2、aioztxlib](#2aioztxlib)

### 二、项目结构

```text
ZTxLib
├── ztxlib              # ztxlib同步模块
│    ├── mariadb        # mariadb连接池
│    ├── rpspring       # 面向切面注解（仿JavaSpring）
│    ├── rpbatis        # mysql中间件注解（仿mybatis）
│    └── smtp           # 邮件发送服务
├── aioztxlib           # ztxlib异步模块
│    ├── aiomysql       # mysql操作类
│    ├── aioredis       # redis操作类
│    └── smtp           # 邮件发送服务
└── requirements.txt    # pip依赖包列表
```

## 三、使用说明

### 1、ztxlib

> 同步ztxlib模块

(1) mariadb

```python
db = mariadb.MariaDB(
    name='pool',  # 连接池名称
    host='localhost',  # 服务器地址
    port=3306,  # 端口号
    user='root',  # 用户名
    password='',  # 密码
    database='',  # 数据库
)
with db.start() as cursor:
    pass  # do something with cursor
```

(2) smtp

```python
# 初始化发件服务器
smtp = smtp.SMTP(
    host='',  # 发件服务器地址
    port=994,  # 端口号
    user='',  # 用户名（发件地址）
    password='',  # 密码
)
with smtp:
    # 发送邮件
    smtp.send(
        subject='',  # 邮件主题
        header_from='',  # 发件人名称
        header_to='',  # 收件人名称
        receivers=[],  # 收件人地址
        mime_parts=[],  # 邮件内容
    )
```

(3) rpspring

面向切面编程模式（仿JavaSpring）

```python
# 实例化对象 FooBar，并将其注册为 Bean
# Bean 的名称为 foo_bar，即将大驼峰命名转换为下划线命名
# 构造函数参数全部使用默认值，无默认值的参数全部为None
@Bean
class FooBar:
    pass
```

```python
# 执行 bar()，并将返回值注册为 Bean
# Bean 的名称为 foo，即函数名
# 参数类别全部使用默认值，无默认值的参数全部为None
@Bean
def foo() -> type:
    pass
```

```python
# 查找名为 foo 的 Bean
# 并将该 Bean 传递给 foo 对象
@Autowired
def foo() -> type: pass
```

```python
@Value("foo.bar")
def bar() -> type: pass
# 从 application.yml 读取配置信息，查找 foo.bar 属性，将值传递给 bar 对象
```

(4) rpbatis

```yaml
# application.yml 样例
database:
  mysql:
    host: "localhost"
    port: 3306
    user: "root"
    password: ""
    database: "mysql"
```

```python
# definition
@Select("SELECT * FROM `${table}` WHERE `id`=#{id}")
def select(table: str, id: int): pass


# usage
data = select(table='t', id=1)


# definition
@Insert("INSERT INTO `${table}` VALUES(#{value1}, #{value2})")
def insert(value1: str, value2: str, table: str): pass


# usage
insert(value1='v1', value2='v2', table='t')


# definition
@Insert("INSERT INTO `${table}` VALUES(#{value1}, #{value2})")
def insert_many(*args: dict, table: str): pass


# uages
insert_many(
    dict(value1='v1', value2='v1'),
    dict(value1='v2', value2='v2'),
    table='t'
)

## Delete, Update 用法同 Insert
## DeleteMany, UpdateMany 用法同 InsertMany
```

### 2、aioztxlib

> 异步ztxlib模块

(1) aiomysql

```python
db = aiomysql.create_pool(
    host='localhost',  # 服务器地址
    port=3306,  # 端口号
    user='root',  # 用户名
    password='',  # 密码
    database='',  # 数据库
)
res1: int = await db.execute("", ...)
res2: dict = await db.fetchone("", ...)
res3: list[dict] = await db.fetchall("", ...)
```

(2) aioredis

```python
pool = aioredis.create_pool(
    address=('localhost', 6379),
    db=0,
)
async with aioredis.start(pool) as redis:
    pass  # to do something
async with aioredis.lock(
        pool=pool,
        name="lock",
        wait_timeout=5,
        timeout=30,
) as lock:
    async with aioredis.start(pool) as redis:
        pass  # to do something
```

(3) aiosmtp

```python
# 初始化发件服务器
smtp = aiosmtp.SMTP(
    host='',  # 发件服务器地址
    port=994,  # 端口号
    user='',  # 用户名（发件地址）
    password='',  # 密码
)
with smtp:
    # 发送邮件
    smtp.send(
        subject='',  # 邮件主题
        header_from='',  # 发件人名称
        header_to='',  # 收件人名称
        receivers=[],  # 收件人地址
        mime_parts=[],  # 邮件内容
    )
```
