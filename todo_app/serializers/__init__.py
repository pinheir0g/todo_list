from flask_pydantic_spec import FlaskPydanticSpec

spec = FlaskPydanticSpec("flask", title="To-Do List")


def init_app(app):
    spec.init_app(app)
