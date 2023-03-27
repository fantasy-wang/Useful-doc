## Use sqlAlchemy to create the database if it not exists

### config engine，create sqlalchemy and database connection
### 配置引擎，创建sqlalchemy和数据库的链接
```
pip install sqlalchemy-utils

from sqlalchemy import create_engine
engine = create_engine("数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名")
engine = create_engine("mysql+pymysql://root:密码@机器地址:3306/数据库名称?charset=utf8&autocommit=true", echo=True, max_overflow=5,
pool_recycle=60, pool_pre_ping=True)
```


### judge whether database exists, if not then create
### 判断数据库是否存在，不存在则创建
```
if not database_exists(engine.url):
    create_database(engine.url)
```


### if not add this judge logical, if database not exists, there will be this error for create database
### 如果不增加此判断逻辑，数据库不存在，创建表时会以下报错
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1049, "Unknown database 'online_test'")
 