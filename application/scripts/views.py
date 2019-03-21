from application import app, db
from flask import render_template, request, url_for, redirect
from application.scripts.models import Script

@app.route("/scripts", methods=["GET"])
def script_list():
    return render_template("scripts/list.html", scripts = Script.query.all())

@app.route("/scripts/new/")
def script_form():
    return render_template("scripts/new.html")

@app.route("/scripts/", methods=["POST"])
def scripts_create():
    s = Script(request.form.get("name"), 
                request.form.get("author"), 
                request.form.get("language"), 
                request.form.get("content"))

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("script_list"))
