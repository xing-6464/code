# 运行模式
DEBUG = True

# 链接数据库信息
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'pdx646464'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'todolist'

# 配置数据库
SQLALCHEMY_DATABASE_URI = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8'
