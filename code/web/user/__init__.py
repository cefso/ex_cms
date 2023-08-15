# 创建flask app
def init_app(app):
    # 引入蓝图
    from . import user
    app.register_blueprint(user.bp)

    # 引入models
    from .models import User

    return app
