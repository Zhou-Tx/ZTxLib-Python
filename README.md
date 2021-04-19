# ZTxLib

## Copyright ©Zhou Tianxing

### 一、目录

* [一、目录](#一目录)
* [二、项目结构](#二项目结构)
* [三、使用说明](#三使用说明)
  * [1、ZTxLib](#1ztxlib)
  * [1.1、接口说明](#11接口说明)
  * [1.2、安装方法](#12安装方法)
  * [2、database](#2database)
  * [2.1、接口说明](#21接口说明)
  * [2.2、使用方法](#22使用方法)
  * [3、utils](#3utils)
  * [3.1、接口说明](#31接口说明)
  * [3.2、使用方法](#32使用方法)

### 二、项目结构

```text
ZTxLib-Python
├── ZTxLib                  # 可安装的ztxlib模块
│  ├── setup               # 安装模块
│  │ ├── __main__.py       # 模块入口
│  │ ├── _classifiers.py   # 分类器列表
│  │ ├── _install.py       # 待装入的模块
│  │ ├── _packages_.py     # 模块列表
│  │ ├── classifiers.txt   # 分类器名称
│  │ └── install.txt       # 待装入的模块名
│  └── ztxlib              # ztxlib模块
│    ├── mariadb           # mariadb连接池
│    ├── rpspring          # 面向切面注解（仿JavaSpring）
│    ├── rpbatis           # mysql中间件注解（仿mybatis）
│    └── smtp              # 邮件发送服务
├── database                # 数据库初步封装（无连接池）
│  ├── __init__.py         # 
│  ├── _mysql.py           # pymysql初步封装
│  └── _sqlite.py          # sqlite初步封装
├── utils                   # 工具类
│  ├── __init__.py
│  └── _properties         # properties文件解析
└── requirements.txt        # pip依赖包列表
```

## 三、使用说明

### 1、ZTxLib

该模块为完整可安装类库

#### 1.1、接口说明

(1) mariadb

```python
db = MariaDB(
    name: str = 'pool',
    host: str = 'localhost',
    port: int = 3306,
    user: str = 'root',
    password: str = '',
    database: str = '',
)
connection, cursor = db.get_connection_cursor()
try:
    pass  # do something with cursor
finally:
    cursor.close(), connection.close()
```

(2) rpspring

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

(3) rpbatis

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

(4) smtp

```python
# 初始化发件服务器
smtp = SMTP(
    host='',    # 发件服务器地址
    port=994,   # 发件服务器端口号
    user='',    # 用户名（发件人地址）
    password='' # 密码
)
# 发送邮件
smtp.send(
    subject='',     # 邮件主题
    header_from=''  # 发件人名称
    header_to=''    # 收件人名称
    receivers=[]    # 收件人地址
    mime_parts=[]   # 邮件内容
)
```

#### 1.2、安装方法

(1) 编辑`install.txt`, 可选模块列表如下：

```text
mariadb
rpspring
rpbatis
smtp
```

(2) 使用终端命令安装至当前环境

```shell
# 可以使用
# ./env/Script/activate [Windows]
# 或
# source env/bin/activate [Linux]
# 激活虚拟环境
cd ZTxLib
python -m setup install
```

### 2、database

该模块为部分数据库初步封装操作类库（无连接池，无性能优化）

#### 2.1、接口说明

（略）

#### 2.2、使用方法

该模块未使用 setuptools 工具打包，可直接复制到项目路径下使用

### 3、utils

该模块为其他工具类，包括 properties 文件解析类

#### 3.1、接口说明

(1) properties

```python
# 输入str或bytes类型的properties格式内容，返回信息内容字典表
def loads(s: Union[str, bytes], *args, **kwargs) -> dict: pass
```

```python
# 输入properties文件指针，读取文件内容，返回信息内容字典表
def load(fp: IO, *args, **kwargs) -> dict: pass
```

#### 3.2、使用方法

该模块未使用 setuptools 工具打包，可直接复制到项目路径下使用
