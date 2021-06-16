from models.user import User
from db.run_sql import run_sql
import repositories.request_repository as request_repository


def save(user):
    sql = "INSERT INTO users( username, bio ) VALUES ( %s, %s ) RETURNING id"
    values = [user.username, user.bio]
    results = run_sql(sql, values)
    user.id = results[0]["id"]


def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)


def select_all():
    results = run_sql("SELECT * FROM users")
    users = []
    for row in results:
        user = User(row["username"], row["bio"], row["id"])
        users.append(user)
    return users


def select(id):
    sql = "SELECT * FROM users WHERE id = %s"
    results = run_sql(sql, [id])
    if len(results) > 0:
        result = results[0]
        user = User(result["username"], result["bio"], result["id"])
        return user
    return None


def update(user):
    sql = "UPDATE users SET username = %s, bio = %s WHERE id = %s"
    values = [user.username, user.bio, user.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM users where id = %s"
    run_sql(sql, [id])
