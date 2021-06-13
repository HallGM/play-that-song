from datetime import datetime
from flask import render_template, request, redirect, Blueprint
from models.request import Request
import repositories.request_repository as request_repository
import repositories.song_repository as song_repository

requests_blueprint = Blueprint("requests", __name__)

# INDEX
@requests_blueprint.route("/requests")
def requests():
    requests = request_repository.select_all()
    return render_template("requests/index.html", requests=requests )

# NEW
@requests_blueprint.route("/requests/new")
def new_request():
    return ""



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


