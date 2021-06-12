from flask import Flask, render_template, request, redirect, Blueprint
from models.user import User
import repositories.user_repository as user_repository
import repositories.artist_repository as artist_repository

users_blueprint = Blueprint("users", __name__)

# INDEX
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    print([vars(item) for item in user_repository.select_all()])
    return render_template("/users/index.html", users=users)

# SHOW
@users_blueprint.route("/users/<id>")
def show_user(id):
    user = user_repository.select(id)
    return render_template("/users/show.html", user=user)

# CREATE
@users_blueprint.route("/users", methods=["POST"])
def create_user():
    form = request.form
    new_user = User(form['username'], form['bio'])
    user_repository.save(new_user)
    return redirect("/users")

# EDIT
@users_blueprint.route("/users/<id>/edit")
def edit_user(id):
    user = user_repository.select(id)
    return render_template("/users/edit.html", user=user)

# UPDATE
@users_blueprint.route("/users/<id>", methods=["POST"])
def update_user(id):
    form = request.form
    user = user_repository.select(id)
    user.username = form['username']
    user.bio = form['bio']
    user_repository.update(user)
    return redirect(f"/users/{id}")
    