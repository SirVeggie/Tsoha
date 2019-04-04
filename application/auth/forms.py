from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3)])
    password = PasswordField("Password", [validators.Length(min=1)])

    class Meta:
        csrf = False