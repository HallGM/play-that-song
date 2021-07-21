from models.artist import Artist
from db.run_sql import run_sql

# DEFINE Function save(artist)
def save(artist):
    # SAVE (SQL command: insert artist into database and return id) IN sql
    sql = "INSERT INTO artists( name ) VALUES ( %s ) RETURNING id"
    # SAVE [name of artist] IN values
    values = [artist.name]
    # RUN command and SAVE returned id IN results
    results = run_sql(sql, values)
    # ADD id TO artist
    artist.id = results[0]["id"]


def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)


def select_all():
    results = run_sql("SELECT * FROM artists")
    artists = [Artist(row["name"], row["id"]) for row in results]
    return artists


def select(id):
    sql = "SELECT * FROM artists WHERE id = %s"
    results = run_sql(sql, [id])
    if len(results) > 0:
        result = results[0]
        artist = Artist(result["name"], result["id"])
        return artist
    return None
