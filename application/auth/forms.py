from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, ValidationError
from application.auth.models import User

def user_exists_check(form, field):
    u = User.query.filter_by(username=form.username.data).all()
    if u:
        raise ValidationError('- A user by that name already exists -')

def name_password_match(form, field):
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        raise ValidationError('- Wrong username or password -')

class SigninForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3
                                        , message='- Username has to be 3-20 characters long -')
                                     , validators.Length(max=20
                                        , message='- Username has to be 3-20 characters long -')
                                     , validators.Regexp('^\w*$'
                                        , message='- Only numbers and letters allowed -')
                                     , user_exists_check])
    password = PasswordField("Password", [validators.Length(min=3
                                        , message='- Password has to be at least 3 characters long -')])

    class Meta:
        csrf = False

class LoginForm(FlaskForm):
    username = StringField("Username", [name_password_match])
    password = PasswordField("Password")

    class Meta:
        csrf = False