# 创建flask app
def init_app(app):
    # 引入蓝图
    from . import alert
    app.register_blueprint(alert.bp)

    # 引入models

    return app
