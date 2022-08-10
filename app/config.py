class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/test.db?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    JSON_AS_ASCII = False
    DEBUG = True