from console import populate_db
from datetime import datetime, time
from flask import render_template, request, redirect, Blueprint
from models.request import Request
import repositories.request_repository as request_repository
import repositories.song_repository as song_repository
import repositories.user_repository as user_repository

requests_blueprint = Blueprint("requests", __name__)

# INDEX
@requests_blueprint.route("/requests")
def requests():
    requests = request_repository.select_all()
    return render_template(
        "requests/index.html", requests=requests, selected="requests"
    )


# NEW
@requests_blueprint.route("/requests/new")
def new_request():
    songs = song_repository.select_all()
    users = user_repository.select_all()
    return render_template("requests/new.html", songs=songs, users=users)


# UPDATE
@requests_blueprint.route("/requests", methods=["POST"])
def update_request():
    form = request.form
    song = song_repository.select(form["song_id"])
    user = user_repository.select(form["user_id"])
    new_request = Request(song, user, datetime.now())
    request_repository.save(new_request)
    return redirect("/requests")


# MARK AS PLAYED
@requests_blueprint.route("/requests/<id>/play", methods=["POST"])
def request_play(id):
    song_request = request_repository.select(id)
    song_request.mark_as_played()
    request_repository.update(song_request)
    song_request.song.last_played = datetime.now()
    song_repository.update(song_request.song)
    return redirect("/requests")


# MARK AS UNPLAYED
@requests_blueprint.route("/requests/<id>/unplay", methods=["POST"])
def request_unplay(id):
    song_request = request_repository.select(id)
    song_request.mark_as_unplayed()
    request_repository.update(song_request)
    return redirect("/requests")

@requests_blueprint.route("/populate")
def populate():
    populate_db()
    return "done"