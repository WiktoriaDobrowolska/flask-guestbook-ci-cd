import os
 
class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'myapp_mysql')
    MYSQL_USER = os.getenv('MYSQL_USER', 'user')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password')
    MYSQL_DB = os.getenv('MYSQL_DATABASE', 'mydb')
    MYSQL_CURSORCLASS = 'DictCursor'  
