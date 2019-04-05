from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.scripts.models import Script
from application.comments.models import Comment

@app.route("/users/mypage", methods=["GET"])
@login_required
def my_page():
    scripts = Script.query.filter_by(author_id=current_user.id).all()
    comments = Comment.query.filter_by(author_id=current_user.id).all()
    return render_template("users/mypage.html",
                            user=current_user,
                            scripts=scripts,
                            comments=comments)