from models.user import User
from db.run_sql import run_sql

def save(user):
    sql = "INSERT INTO users( username, bio ) VALUES ( %s, %s ) RETURNING id"
    values = [user.username, user.bio]
    results = run_sql( sql, values )
    user.id = results[0]['id']

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def select_all():
    results = run_sql("SELECT * FROM users")
    users = [User(row['username'], row['bio'], [], row['id']) for row in results]
    return users

def select(id):
    sql = "SELECT * FROM users WHERE id = %s"
    results = run_sql(sql, [id])
    if len(results) > 0:
        result = results[0]
        user = User(result['username'], result['bio'], [], result['id'])
        return user
    return None