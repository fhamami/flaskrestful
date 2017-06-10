import os

class Config(object):
    """ Parent configuration class. """
    DEBUG = False
    CSRF_ENABLE = True
    SECRET_KEY = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """ Configuration for development """
    DEBUG = True

class TestingConfig(Config):
    """ Configuration for testing, with a separate test database. """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://urestful:marimakan@172.17.0.2/restful_test_db'
    DEBUG = True
    # https://stackoverflow.com/questions/26647032/py-test-to-test-flask-register-assertionerror-popped-wrong-request-context
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class StagingConfig(Config):
    """ Configuration for staging """
    DEBUG = True

class ProductionConfig(Config):
    """ Configuration for production """
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
