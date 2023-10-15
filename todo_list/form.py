import wtforms as wtf
from flask_wtf import FlaskForm


class TaskForm(FlaskForm):
    title = wtf.StringField("Titulo", [wtf.validators.DataRequired()])
    description = wtf.TextAreaField(
        "Descrição", [wtf.validators.DataRequired()]
    )
