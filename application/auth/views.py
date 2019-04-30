from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User, Userrole
from application.auth.forms import LoginForm, SigninForm

@app.route("/auth/login/", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/login.html", form = form)
    
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
                
    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout/")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/sign-in/", methods = ["GET", "POST"])
def user_create():
    if current_user.is_authenticated:
        return redirect("/")

    if request.method == "GET":
        return render_template("auth/sign-in.html", form = SigninForm())

    form = SigninForm(request.form)

    if not form.validate():
        return render_template("auth/sign-in.html", form = form)

    u = User(form.username.data,
            form.password.data)

    db.session().add(u)
    db.session().commit()

    login_user(u)

    return redirect(url_for("index"))

@app.route("/auth/grant_admin/", methods = ["GET"])
@login_required()
def grant_admin():
    ur = Userrole.query.filter_by(role="ADMIN", user_id=current_user.id).first()
    if ur:
        return redirect("/")

    ur = Userrole("ADMIN", current_user.id)

    db.session().add(ur)
    db.session().commit()

    return redirect("/")