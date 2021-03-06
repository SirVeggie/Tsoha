from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.auth.models import User
from application.scripts.models import Script
from application.comments.models import Comment
from application.favourites.models import Favourite

@app.route("/users/mypage/", methods=["GET"])
@login_required()
def my_page():
    scripts = Script.query.filter_by(author_id=current_user.id).all()
    comments = Comment.query.filter_by(author_id=current_user.id).all()
    favourites = current_user.get_favourites_as_scripts()
    return render_template("users/userpage.html",
                            current_user=current_user,
                            user=current_user,
                            scripts=scripts,
                            comments=comments,
                            favourites=favourites)


@app.route("/users/<user_id>/", methods=["GET"])
def user_page(user_id):
    try:
        user_id = int(user_id)
    except:
        return render_template("errors/error404.html")
    
    user = User.query.get(user_id)
    if not user:
        return render_template("errors/error404.html")

    if current_user.is_authenticated:
        if int(current_user.id) == int(user_id):
            return redirect(url_for("my_page"))

    scripts = Script.query.filter_by(author_id=user_id).all()
    comments = Comment.query.filter_by(author_id=user_id).all()
    return render_template("users/userpage.html",
                            current_user=current_user,
                            user=user,
                            scripts=scripts,
                            comments=comments)

