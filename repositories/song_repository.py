from datetime import datetime
from models.song import Song
import repositories.artist_repository as artist_repository
from db.run_sql import run_sql


def save(song):
    sql = "INSERT INTO songs( title, artist_id, last_played ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [song.title, song.artist.id, song.last_played]
    results = run_sql(sql, values)
    song.id = results[0]["id"]


def delete_all():
    run_sql("DELETE FROM songs")


def select_all():
    results = run_sql("SELECT * FROM songs")
    songs = []
    for row in results:
        artist = artist_repository.select(row["artist_id"])
        time = row["last_played"]
        songs.append(Song(row["title"], artist, time, row["id"]))
    songs.sort(key=lambda song: song.artist.name)
    return songs


def select(id):
    sql = "SELECT * FROM songs WHERE id = %s"
    results = run_sql(sql, [id])

    if len(results) > 0:
        result = results[0]
        artist = artist_repository.select(result["artist_id"])
        song = Song(result["title"], artist, result["last_played"], result["id"])
        return song
    return None


def update(song):
    sql = "UPDATE songs SET title = %s, artist_id = %s, last_played = %s WHERE id = %s"
    values = [song.title, song.artist.id, song.last_played, song.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM songs where id = %s"
    run_sql(sql, [id])


def search(query):
    query = f"%{query}%"
    sql = "SELECT songs.id as song_id, artists.id as artist_id, songs.last_played, songs.title, artists.name FROM songs INNER JOIN artists ON songs.artist_id = artists.id WHERE LOWER(artists.name) LIKE LOWER(%s) OR LOWER(songs.title) LIKE LOWER(%s)"
    values = [query, query]
    results = run_sql(sql, values)
    songs = []
    for row in results:
        artist = artist_repository.select(row["artist_id"])
        time = row["last_played"]
        songs.append(Song(row["title"], artist, time, row["song_id"]))
    songs.sort(key=lambda song: song.artist.name)
    return songs
