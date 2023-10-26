# 创建flask app
def init_app(app):
    # 引入蓝图
    from . import cms
    app.register_blueprint(cms.bp)

    return app
