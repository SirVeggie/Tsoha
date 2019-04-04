from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class CommentForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=3)])
    content = TextAreaField("content", [validators.Length(min=1)])

    class Meta:
        csrf = False