from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class ScriptForm(FlaskForm):
    name = StringField("Script name", [validators.Length(min=4)])
    language = StringField("Language", [validators.Length(min=1)])
    content = TextAreaField("Content", [validators.Length(min=1)])

    class Meta:
        csrf = False