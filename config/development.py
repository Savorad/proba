from . import Config

class Development(Config):
    ENV_TYPE = "Dev"

    DEBUG = True

    DB_NAME = "praksa_2019"
    DB_USER = "sava"
    DB_PASSWD = "sifra"
    DB_HOST = "127.0.0.1"
    DB_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'    