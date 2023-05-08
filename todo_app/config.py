import os


def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', default=None)
    if not os.environ.get('SECRET_KEY'):
        raise Exception("Variável de ambiente SECRET_KEY não encontrada! Configure com 'export SECRET_KEY='sua_key''")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['API_URL'] = 'http://localhost:5000'
