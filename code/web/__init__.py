import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from web.config import config

db = SQLAlchemy()
migrate = Migrate()


# 创建flask app
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # 引入配置文件
    app.config.from_object(config['development'])
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 数据库相关初始化
    db.init_app(app)
    migrate.init_app(app, db)

    # 引入蓝图
    from web import alert
    app.register_blueprint(alert.bp)

    # 引入models

    return app
