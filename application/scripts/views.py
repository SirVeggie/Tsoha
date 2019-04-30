from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_user

from application import app, db, login_required
from application.scripts.models import Script
from application.scripts.forms import ScriptForm
from application.auth.models import User, Userrole
from application.comments.models import Comment
from application.comments.forms import CommentForm
from application.favourites.models import Favourite


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
    if not validate_script_id(script_id):
        return render_template("errors/error404.html")
    
    s = Script.query.get(script_id)
    a = User.query.get(s.author_id)
    cObject = find_comments_with_author_name(script_id)

    userrole = "guest"
    if current_user.is_authenticated and current_user.is_admin():
            userrole = "ADMIN"

    if current_user.is_authenticated:
        f = Favourite.query.filter_by(user_id=current_user.id, script_id=script_id).first()
        if f:
            favourited = True
        else:
            favourited = False
    else:
        favourited = False

    return render_template("scripts/single.html",
                            script=s,
                            current_user=current_user,
                            author=a.username,
                            commentForm=CommentForm(),
                            commentObject=cObject,
                            role=userrole,
                            favourited=favourited)


@app.route("/scripts/<script_id>/delete_comment/<comment_id>/", methods=["GET"])
@login_required()
def comment_delete(script_id, comment_id):
    if not validate_script_id(script_id):
        return render_template("errors/error404.html")
    
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
        return render_template("scripts/new.html", form = form)

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
    if not validate_script_id(script_id):
        return redirect(url_for("script_list"))
    
    s = Script.query.get(script_id)
    s.content = request.form.get("content")
    db.session().commit()

    return redirect("/scripts" + str(script_id) + "/")


@app.route("/scripts/<script_id>/delete/", methods=["POST"])
@login_required()
def script_delete(script_id):
    if not validate_script_id(script_id):
        return redirect(url_for("script_list"))
    
    if s.author_id != current_user.id and not current_user.is_admin():
        return redirect(url_for("script_list"))
    
    s = Script.query.get(script_id)

    delete_comments_on_script(script_id)
    db.session().delete(s)
    db.session().commit()
    return redirect(url_for("script_list"))


@app.route("/scripts/<script_id>/comment/", methods=["POST"])
@login_required()
def comment_create(script_id):
    if not validate_script_id(script_id):
        return redirect(url_for("script_list"))
    
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


@app.route("/scripts/<script_id>/favourite/", methods=["POST"])
@login_required()
def favourite(script_id):
    if not validate_script_id(script_id):
        return redirect(url_for("script_list"))
    
    f = Favourite.query.filter_by(user_id=current_user.id, script_id=script_id).first()
    s = Script.query.get(script_id)
    if f or int(s.author_id) == int(current_user.id):
        return redirect(url_for("script_show", script_id=script_id))

    f = Favourite(current_user.id, script_id)

    db.session().add(f)
    db.session().commit()

    return redirect(url_for("script_show", script_id=script_id))


@app.route("/scripts/<script_id>/unfavourite/", methods=["POST"])
@login_required()
def unfavourite(script_id):
    if not validate_script_id(script_id):
        return redirect(url_for("script_list"))
    
    f = Favourite.query.filter_by(user_id=current_user.id, script_id=script_id).first()
    if not f:
        return redirect(url_for("script_show", script_id=script_id))

    db.session().delete(f)
    db.session().commit()

    return redirect(url_for("script_show", script_id=script_id))
    



#Methods
def validate_script_id(script_id):
    try:
        script_id = int(script_id)
    except:
        return False
    
    s = Script.query.get(script_id)
    if not s:
        return False
    
    return True

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