from todo_app.db import db
from todo_app.db import models  # noqa


def init_app(app):
    @app.cli.command()
    def create_db():
        """Cria o banco de dados"""
        db.create_all()
