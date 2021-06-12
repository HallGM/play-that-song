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