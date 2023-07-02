import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:  # 基本配置类
    SECRET_KEY = os.getenv('SECRET_KEY', 'some secret words')
    ITEMS_PER_PAGE = 10


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = '***REMOVED***'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SCHEDULER_API_ENABLED = True


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
}
