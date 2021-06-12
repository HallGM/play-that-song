from flask import Flask, render_template, request, redirect, Blueprint
from models.song import Song
import repositories.song_repository as song_repository
import repositories.artist_repository as artist_repository

songs_blueprint = Blueprint("songs", __name__)

@songs_blueprint.route("/songs")
def songs():
    songs = song_repository.select_all()
    artists = artist_repository.select_all()
    return render_template("songs/index.html", songs=songs, artists=artists, edit=None)

@songs_blueprint.route("/songs/<id>/edit")
def songs_edit(id):
    songs = song_repository.select_all()
    artists = artist_repository.select_all()
    edit = int(id)
    return render_template("songs/index.html", songs=songs, artists=artists, edit=edit)

@songs_blueprint.route("/songs/<id>", methods=["POST"])
def songs_update(id):
    form = request.form
    song = song_repository.select(id)
    song.title = form['title']
    artist = artist_repository.select(form['artist_id'])
    song.artist = artist
    song_repository.update(song)
    return redirect("/songs")