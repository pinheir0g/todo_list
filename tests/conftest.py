import pytest
from todo_list.app import create_app
from todo_list.db import db


@pytest.fixture(scope='module')
def app():
    """Instance of Main flask app"""
    app = create_app(test_config=True)

    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados para testes
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    """Cliente de teste para interagir com o aplicativo"""
    return app.test_client()
