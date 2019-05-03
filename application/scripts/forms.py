from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class ScriptForm(FlaskForm):
    name = StringField("Script name", [validators.Regexp('.*\w+.*'
                                        , message='- Name must not be empty -')
                                    , validators.Length(max=50
                                        , message='- Name is too long -')])


    language = StringField("Language", [validators.Regexp('.*\w+.*'
                                        , message='- Language must not be empty -')
                                    , validators.Length(max=20
                                        , message='- Language is too long -')])


    content = TextAreaField("Content")

    class Meta:
        csrf = False


class SearchForm(FlaskForm):
    parameter = StringField("Search", [validators.Regexp('\w*'
                                        , message='- Only normal letters, numbers and _ -')
                                    , validators.Length(max=50
                                        , message='- Name is too long -')])

    class Meta:
        csrf = False