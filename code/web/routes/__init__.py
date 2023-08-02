from .alert import bp


def init_app(app):
    app.register_blueprint(alert.bp)
