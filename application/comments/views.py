from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.auth.models import User
from application.scripts.models import Script
from application.comments.models import Comment
from application.comments.forms import CommentForm

@app.route("/comments/<comment_id>/", methods=["GET"])
@login_required()
def comment_show(comment_id):
    comment = Comment.query.get(comment_id)

    if current_user.id != comment.author_id:
        return render_template("errors/error404.html")
    
    return render_template("comments/edit.html",
                            comment=comment,
                            current_user=current_user,
                            commentForm=CommentForm())


@app.route("/comments/<comment_id>/delete/", methods=["GET"])
@login_required()
def comment_delete(comment_id):
    comment = Comment.query.get(comment_id)

    if current_user.id != comment.author_id:
        return redirect("/")
    
    if not comment:
        return redirect("/")

    db.session().delete(comment)
    db.session().commit()
    
    return redirect(url_for("script_show", script_id=comment.script_id))


@app.route("/comments/<comment_id>/edit/", methods=["POST"])
@login_required()
def comment_edit(comment_id):
    comment = Comment.query.get(comment_id)

    if current_user.id != comment.author_id:
        return redirect("/")

    if not comment:
        return redirect("/")

    # If the script this comment belongs to doesn't exist, delete it.
    s = Script.query.get(comment.script_id)
    if not s:
        db.session().delete(comment)
        db.session().commit()
    
    form = CommentForm(request.form)

    if not form.validate():
        return redirect(url_for("comment_show", script_id=comment.id))
    
    comment.title = request.form.get("title")
    comment.content = request.form.get("content")

    db.session().commit()

    return redirect(url_for("comment_show", comment_id=comment.id))