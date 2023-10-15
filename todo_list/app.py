from flask import Flask
from todo_list import config, api, cli, views
from todo_list.db import db, migrate
from todo_list.serializers import spec


def create_app(test_config=None):
    """Factory principal"""
    app = Flask(__name__)
    if test_config is None:
        config.init_app(app)
    else:
        config.init_app(app, test_config=True)
    db.init_app(app)
    migrate.init_app(app, db)
    spec.register(app)
    cli.init_app(app)
    api.init_app(app)
    views.init_app(app)
    return app
