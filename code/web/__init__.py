import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_siwadoc import SiwaDoc

from web.config import config

db = SQLAlchemy()
migrate = Migrate()
siwa = SiwaDoc(title="siwadocapi", description="一个自动生成openapi文档的库")


# 创建flask app
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # siwa
    siwa.init_app(app)

    # 引入配置文件
    app.config.from_object(config['development'])
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the health config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 数据库相关初始化
    db.init_app(app)
    migrate.init_app(app, db)

    from . import alert, health
    alert.init_app(app)
    health.init_app(app)

    return app
