from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application import app, db
from application.scripts.models import Script
from application.scripts.forms import ScriptForm
from application.auth.models import User
from application.comments.models import Comment


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
    s = Script.query.get(script_id)
    a = User.query.get(s.author_id)
    c = Comment.query.filter_by(script_id=script_id).all()
    return render_template("scripts/single.html",
                            script=s,
                            author=a.username,
                            comments=c)


# POST methods

@app.route("/scripts/", methods=["POST"])
@login_required
def script_create():
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

@app.route("/scripts/<script_id>/delete", methods=["POST"])
@login_required
def script_delete(script_id):
    s = Script.query.get(script_id)
    if not s:
            return redirect(url_for("script_list"))

    if s.author_id == current_user.id:
        db.session().delete(s)
        db.session().commit()
        return redirect(url_for("script_list"))
        
    return render_template("/scripts/single.html",
                            script=s,
                            author=User.query.get(s.author_id).username,
                            delError="- Only the author can delete this script -")