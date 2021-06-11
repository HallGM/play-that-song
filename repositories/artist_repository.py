from models.artist import Artist
from db.run_sql import run_sql

def save(artist):
    sql = "INSERT INTO artists( name ) VALUES ( %s ) RETURNING id"
    values = [artist.name]
    results = run_sql( sql, values )
    artist.id = results[0]['id']

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select_all():
    results = run_sql("SELECT * FROM artists")
    artists = [Artist(row['name'], row['id']) for row in results]
    return artists