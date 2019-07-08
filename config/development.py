from . import Config

class Developmnet(Config):
    ENV_TYPE = "Dev"

    DEBUG = True
    FLASK_HOST = 'localhost'
    PORT = "8000"

    DB_NAME = None
    DB_USER = None
    DB_PASSWD = None
    DB_HOST = None
    DB_PORT = None
    