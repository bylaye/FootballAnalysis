import configparser
import os

DIRECTORY = os.path.dirname(__file__)
config_file = os.path.join(DIRECTORY, 'config.ini')
config = configparser.ConfigParser()
config.read(config_file)

NAME_DIR_DATASET = config.get('dirs', 'DIR_NAME_DATASET')

# db engine mysql/mariadb
mysql = 'db_mysql'
MYSQL_USER = config.get(mysql, 'USER')
MYSQL_PASSWORD = config.get(mysql, 'PASSWORD')
MYSQL_HOST = config.get(mysql, 'HOST')
MYSQL_PORT = config.get(mysql, 'PORT')
MYSQL_DB_NAME = config.get(mysql, 'DB_NAME')
