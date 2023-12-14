from os import environ, getenv
from dotenv import load_dotenv

load_dotenv()  # Load .env environment variables


modes: dict = {'PRODUCTION': 'ProductionConfig',
               'DEVELOP': 'DevelopmentConfig',
               'TEST': 'TestingConfig'}


class Config(object):
    """
    Default configuration.
    """

    ENV = 'production'
    DEBUG = False
    TESTING = False
    DB_NAME = "production-db"
    DB_USERNAME = getenv("DB_USERNAME")
    DB_PASSWORD = getenv("DB_PASSWORD")
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:///' + DB_NAME + '.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True


class ProductionConfig(Config):
    """
    Production configuration.
    """

    pass


class DevelopmentConfig(Config):
    """
    Development configuration.
    """

    ENV = 'development'
    DEBUG = True
    DB_NAME = "development-db"
    DB_USERNAME = "userjw"
    DB_PASSWORD = "1q2w3e4r"
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:///' + DB_NAME + '.db')
    LOG_LEVEL = 'DEBUG'


class TestingConfig(Config):
    """
    Testing configuration.
    """

    ENV = 'testing'
    TESTING = True
    DB_NAME = "testing-db"
    DB_USERNAME = "userjw"
    DB_PASSWORD = "1q2w3e4r"
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:///' + DB_NAME + '.db')
    LOG_LEVEL = 'DEBUG'
