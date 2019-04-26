from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///scripts.db"
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)


#Login
from application.auth.models import User, Userrole
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# login roles
from functools import wraps
from flask_login import current_user

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
          
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


# Content
from application import views
from application.scripts import models
from application.scripts import views
from application.auth import models
from application.auth import views
from application.comments import models
from application.comments import views
from application.users import views



try:
    db.create_all()
except:
    pass



u = User.query.filter_by(username="Admin").first()
if not u:
    u = User(username="Admin", password="1234")

    db.session().add(u)
    db.session().commit()

    u = User.query.filter_by(username="Admin").first()
    ur = Userrole("ADMIN", u.id)

    db.session().add(ur)
    db.session().commit()