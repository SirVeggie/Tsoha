from flask import render_template, request, url_for, redirect
from flask_login import current_user

from application import app, db, login_required
from application.scripts.models import Script
from application.scripts.forms import ScriptForm
from application.auth.models import User
from application.comments.models import Comment
from application.comments.forms import CommentForm


# GET methods

@app.route("/scripts/", methods=["GET"])
def script_list():
    return render_template("scripts/list.html", scripts = Script.query.all())


@app.route("/scripts/new/", methods=["GET"])
@login_required()
def script_form():
    return render_template("scripts/new.html", form = ScriptForm())


@app.route("/scripts/<script_id>/", methods=["GET"])
def script_show(script_id):
    s = Script.query.get(script_id)
    a = User.query.get(s.author_id)
    cObject = find_comments_with_author_name(script_id)
    
    return render_template("scripts/single.html",
                            script=s,
                            current_user=current_user,
                            author=a.username,
                            commentForm=CommentForm(),
                            commentObject=cObject)


@app.route("/scripts/<script_id>/delete_comment/<comment_id>", methods=["GET"])
@login_required()
def comment_delete(script_id, comment_id):
    c = Comment.query.get(comment_id)
    if not c:
        return redirect(url_for("script_show", script_id=script_id))

    if c.author_id == current_user.id:
        db.session().delete(c)
        db.session().commit()
    
    return redirect(url_for("script_show", script_id=script_id))



# POST methods

@app.route("/scripts/", methods=["POST"])
@login_required()
def script_create():
    form = ScriptForm(request.form)

    if not form.validate():
        return render_template("scripts/new.html", form = form, 
                        error = "- Name must be at least 5 characters long -\n"
                              + "- Language and content must not be empty -")
    
    s = Script.query.filter_by(name=form.name.data).all()
    if s:
        return render_template("scripts/new.html", form = form, 
                        error = "- A script by that name already exists -")

    s = Script(form.name.data,
            form.language.data,
            form.content.data)
    s.author_id = current_user.id
    

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("script_list"))


@app.route("/scripts/<script_id>/", methods=["POST"])
@login_required()
def script_modify(script_id):
    s = Script.query.get(script_id)
    s.content = request.form.get("content")
    db.session().commit()

    return redirect("/scripts/" + str(script_id) + "/")


@app.route("/scripts/<script_id>/delete", methods=["POST"])
@login_required()
def script_delete(script_id):
    s = Script.query.get(script_id)
    if not s:
        return redirect(url_for("script_list"))

    if s.author_id != current_user.id:
        return redirect(url_for("script_list"))
    
    delete_comments_on_script(script_id)
    db.session().delete(s)
    db.session().commit()
    return redirect(url_for("script_list"))


@app.route("/scripts/<script_id>/comment", methods=["POST"])
@login_required()
def comment_create(script_id):
    form = CommentForm(request.form)

    if not form.validate():
        return redirect(url_for("script_show", script_id=script_id))
    
    c = Comment(form.title.data,
                form.content.data)
    c.author_id = current_user.id
    c.script_id = script_id

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("script_show", script_id=script_id))



#Methods
def find_comments_with_author_name(script_id):
    comments = Comment.query.filter_by(script_id=script_id).all()

    response = []
    for c in comments:
        author = User.query.get(c.author_id).username
        response.append({"comment":c, "author":author})
    
    return response

def delete_comments_on_script(script_id):
    coms = Comment.query.filter_by(script_id=script_id).all()
    for c in coms:
        db.session().delete(c)
    db.session().commit()