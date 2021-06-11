from datetime import datetime
from models.song import Song
import repositories.artist_repository as artist_repository
from db.run_sql import run_sql

def save(song):
    sql = "INSERT INTO songs( title, artist_id, last_played ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [song.title, song.artist.id, song.last_played]
    results = run_sql( sql, values )
    song.id = results[0]['id']

def delete_all():
    run_sql("DELETE FROM songs")

def select_all():
    results = run_sql("SELECT * FROM songs")
    songs = []
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        time = row['last_played']
        songs.append(Song(row['title'], artist, time, row['id']))
    return songs