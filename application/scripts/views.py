from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application import app, db
from application.scripts.models import Script
from application.scripts.forms import ScriptForm
from application.auth.models import User


# GET methods

@app.route("/scripts/", methods=["GET"])
def script_list():
    return render_template("scripts/list.html", scripts = Script.query.all())

@app.route("/scripts/new/", methods=["GET"])
@login_required
def script_form():
    return render_template("scripts/new.html", form = ScriptForm())

@app.route("/scripts/<script_id>/", methods=["GET"])
def script_show(script_id):
    this_script = Script.query.get(script_id)
    author = User.query.get(this_script.author_id)
    return render_template("scripts/single.html",
                            script=this_script,
                            author=author.username)


# POST methods

@app.route("/scripts/", methods=["POST"])
@login_required
def scripts_create():
    form = ScriptForm(request.form)

    if not form.validate():
        return render_template("scripts/new.html", form = form, 
                        error = "- Name must be at least 5 characters long -\n"
                              + "- Language and content must not be empty -")

    s = Script(form.name.data,
            form.language.data,
            form.content.data)
    s.author_id = current_user.id
    

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("script_list"))

@app.route("/scripts/<script_id>/", methods=["POST"])
@login_required
def script_modify(script_id):
    s = Script.query.get(script_id)
    s.content = request.form.get("content")
    db.session().commit()

    return redirect("/scripts/" + str(script_id) + "/")