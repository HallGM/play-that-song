from flask import render_template, request, redirect, Blueprint
import repositories.song_repository as song_repository
import repositories.request_repository as request_repository
import repositories.user_repository as user_repository
from models.request import Request
from datetime import datetime

ui_home_blueprint = Blueprint("ui_home", __name__)

# HOME
@ui_home_blueprint.route('/user-interface/<id>')
def ui_home(id):
    return render_template('/user_interface/index.html', id=id, back_button=None)

# SONGS
@ui_home_blueprint.route('/user-interface/<id>/songs')
def ui_songs(id):
    songs = song_repository.select_all()
    return render_template('/user_interface/songs.html', id=id, songs=songs, back_button=f"/user-interface/{id}")

# CREATE REQUEST 
@ui_home_blueprint.route("/user-interface/<user_id>/request/<song_id>", methods=["POST"])
def update_request(user_id, song_id):
    song = song_repository.select(song_id)
    user = user_repository.select(user_id)
    new_request = Request(song, user, datetime.now())
    request_repository.save(new_request)
    return redirect(f"/user-interface/{user_id}/congrats")

# REQUESTS
@ui_home_blueprint.route('/user-interface/<id>/requests')
def ui_requests(id):
    requests = request_repository.select_all()
    return render_template("/user_interface/requests.html", id=id, requests=requests, back_button=f"/user-interface/{id}")

# MY REQUESTS
@ui_home_blueprint.route('/user-interface/<id>/my-requests')
def ui_my_requests(id):
    requests = request_repository.select_by_user(id)
    return render_template("/user_interface/requests.html", id=id, requests=requests, back_button=f"/user-interface/{id}")

# MY PROFILE
@ui_home_blueprint.route("/user-interface/<id>/profile")
def ui_profile(id):
    user = user_repository.select(id)
    requests = request_repository.select_by_user(id)
    return render_template("/user_interface/user/profile.html", user=user, requests=requests, hide_profile=True, back_button=f"/user-interface/{id}")

# EDIT PROFILE
@ui_home_blueprint.route("/user-interface/<id>/profile/edit")
def ui_edit_profile(id):
    user = user_repository.select(id)
    return render_template("/user_interface/user/edit-profile.html", user=user, hide_profile=True, back_button=f"/user-interface/{id}/profile")

# UPDATE PROFILE
@ui_home_blueprint.route("/user-interface/<id>/profile", methods=["POST"])
def ui_update_profile(id):
    form = request.form
    user = user_repository.select(id)
    user.username = form['username']
    user.bio = form['bio']
    user_repository.update(user)
    return redirect(f"/user-interface/{id}/profile")

# CONGRATS
@ui_home_blueprint.route("/user-interface/<id>/congrats")
def ui_congrats(id):
    return render_template("user_interface/congrats.html", id=id, back_button=None)

# SEARCH
@ui_home_blueprint.route("/user-interface/<id>/songs/search", methods=["POST"])
def ui_search_songs(id):
    form = request.form
    songs = song_repository.search(form['search'])
    no_songs = len(songs) == 0
    return render_template('/user_interface/songs.html', id=id, songs=songs, back_button=f"/user-interface/{id}", no_songs=no_songs, show_clear=True)