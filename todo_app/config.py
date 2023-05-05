def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
    app.config.from_pyfile(".secrets.py")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
