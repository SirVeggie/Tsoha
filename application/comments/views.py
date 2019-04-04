from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from forms import CommentForm
from models import Comment


@app.route("/comment/create/<script_id>", methods=["POST"])
@login_required
def comment_create(script_id):
    form = CommentForm(request.form)

    if not form.validate():
        return render_template("scripts/single.html", form = form,
                                error = "")
    
    c = Comment(form.title.data,
                form.content.data)
    c.author_id = current_user.id
    c.script_id = script_id

    db.session().add(c)
    db.session().commit()