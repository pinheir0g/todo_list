from .main import bp_render


def init_app(app):
    app.register_blueprint(bp_render)
