from flask import Flask
from todo_app import config, api, cli, views
from todo_app.db import db, migrate
from todo_app.serializers import spec


def create_app():
    """Factory principal"""
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    spec.register(app)
    cli.init_app(app)
    api.init_app(app)
    views.init_app(app)
    return app
