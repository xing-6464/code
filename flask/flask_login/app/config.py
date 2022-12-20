# 运行模式
DEBUG = True

# 链接数据库信息
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = ''
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'html_info'

# 配置数据库
SQLALCHEMY_DATABASE_URI = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8'

# 配置登录密钥
SECRET_KEY = '281b918a-40aa-41cf-bb75-2c8db9a87b6b'
