import repositories.song_repository as song_repository
import repositories.user_repository as user_repository
from models.request import Request
from db.run_sql import run_sql

def save(request):
    sql = "INSERT INTO requests( song_id, user_id, time, played ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [request.song.id, request.user.id, request.time, request.played]
    results = run_sql( sql, values )
    request.id = results[0]['id']

def delete_all():
    sql = "DELETE FROM requests"
    run_sql(sql)

def select_all():
    results = run_sql("SELECT * FROM requests")
    requests = []
    for row in results:
        song = song_repository.select(row['song_id'])
        user = user_repository.select(row['user_id'])
        request = Request(song, user, row['time'], row["id"], row['played'],)
        requests.append(request)
    return requests

def select(id):
    sql = "SELECT * FROM requests WHERE id = %s"
    results = run_sql(sql, [id])
    if len(results) > 0:
        result = results[0]
        song = song_repository.select(result['song_id'])
        user = user_repository.select(result['user_id'])
        request = Request(song, user, result['time'], result['id'], result['played'])
        return request
    return None

def update(request):
    sql = "UPDATE requests SET song_id = %s, user_id = %s, time = %s, played = %s WHERE id = %s"
    values = [request.song.id, request.user.id, request.time, request.played, request.id]
    run_sql(sql, values)

def select_by_user(user_id):
    sql = "SELECT * from requests WHERE user_id = %s"
    results = run_sql(sql, [user_id])
    requests = []
    for result in results:
        song = song_repository.select(result['song_id'])
        user = user_repository.select(result['user_id'])
        request = Request(song, user, result['time'], result['id'], result['played'])
        requests.append(request)
    return requests
