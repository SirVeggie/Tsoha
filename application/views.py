from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html", active_count=User.number_of_active_users())

@app.errorhandler(404)
def handler_404(e):
    return render_template("errors/error404.html")