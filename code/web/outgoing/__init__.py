# 创建flask app
def init_app(app):
    # 引入蓝图
    from . import outgoing
    app.register_blueprint(outgoing.bp)

    # 引入models
    # from .models import AliyunAlert

    return app
