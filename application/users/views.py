from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.auth.models import User
from application.scripts.models import Script
from application.comments.models import Comment

@app.route("/users/mypage", methods=["GET"])
@login_required()
def my_page():
    scripts = Script.query.filter_by(author_id=current_user.id).all()
    comments = Comment.query.filter_by(author_id=current_user.id).all()
    return render_template("users/userpage.html",
                            user=current_user,
                            scripts=scripts,
                            comments=comments)


@app.route("/users/<user_id>", methods=["GET"])
def user_page(user_id):
    scripts = Script.query.filter_by(author_id=user_id).all()
    comments = Comment.query.filter_by(author_id=user_id).all()
    user = User.query.get(user_id)
    return render_template("users/userpage.html",
                            user=user,
                            scripts=scripts,
                            comments=comments)