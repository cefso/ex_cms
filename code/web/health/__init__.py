# 创建flask app
def init_app(app):
    # 引入蓝图
    from . import health
    app.register_blueprint(health.bp)

    # 引入models

    return app
