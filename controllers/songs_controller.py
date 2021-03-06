from flask import render_template, request, redirect, Blueprint
from models.song import Song
import repositories.song_repository as song_repository
import repositories.artist_repository as artist_repository

songs_blueprint = Blueprint("songs", __name__)

# INDEX
@songs_blueprint.route("/songs")
def songs():
    songs = song_repository.select_all()
    artists = artist_repository.select_all()
    return render_template(
        "songs/index.html", songs=songs, artists=artists, edit=None, selected="songs"
    )


# EDIT
@songs_blueprint.route("/songs/<id>/edit")
def songs_edit(id):
    songs = song_repository.select_all()
    artists = artist_repository.select_all()
    edit = int(id)
    no_songs = len(songs) == 0
    return render_template(
        "songs/index.html", songs=songs, artists=artists, edit=edit, son_songs=no_songs
    )


# UPDATE
@songs_blueprint.route("/songs/<id>", methods=["POST"])
def songs_update(id):
    form = request.form
    song = song_repository.select(id)
    song.title = form["title"]
    artist = artist_repository.select(form["artist_id"])
    song.artist = artist
    song_repository.update(song)
    return redirect("/songs")


# DESTROY
@songs_blueprint.route("/songs/<id>/delete", methods=["POST"])
def delete_song(id):
    song_repository.delete(id)
    return redirect("/songs")


# NEW
@songs_blueprint.route("/songs", methods=["POST"])
def new_song():
    form = request.form
    artist = artist_repository.select(form["artist_id"])
    new_song = Song(form["title"], artist)
    song_repository.save(new_song)
    return redirect("/songs")


# SEARCH
@songs_blueprint.route("/songs/search", methods=["POST"])
def search_songs():
    form = request.form
    songs = song_repository.search(form["search"])
    artists = artist_repository.select_all()
    no_songs = len(songs) == 0
    return render_template(
        "songs/index.html",
        songs=songs,
        artists=artists,
        edit=None,
        show_clear=True,
        no_songs=no_songs,
    )
