from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class ScriptForm(FlaskForm):
    name = StringField("Script name", [validators.Regexp('\w+'
                                        , message='- Name must not be empty -')])
    language = StringField("Language", [validators.Regexp('\w+'
                                        , message='- Language must not be empty -')])
    content = TextAreaField("Content")

    class Meta:
        csrf = False