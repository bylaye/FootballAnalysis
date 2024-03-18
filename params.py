import configparser
import os

DIRECTORY = os.path.dirname(__file__)
config_file = os.path.join(DIRECTORY, 'config.ini')
config = configparser.ConfigParser()
config.read(config_file)

NAME_DIR_DATASET = config.get('dirs', 'DIR_NAME_DATASET')

