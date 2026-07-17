import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    TESTING = False
class ProductionConfig(Config):
    DATABSE_URL = 'mysql://user@localhost/foo'
class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = 'sqlite:///development.db'
class TestingConfig(Config):
    TESTING = True
    DATABASE_URL = 'sqlite:///testing.db'