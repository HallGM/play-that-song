import os
import psycopg2
import psycopg2.extras as ext

if ('DATA_URL' in os.environ):
    DATABASE_URL = os.environ['DATABASE_URL']
else:
    DATABASE_URL = "dbname='song_requestor'"

def run_sql(sql, values=None):
    connection = None
    results = []

    try:
        connection = psycopg2.connect("dbname='song_requestor'")
        cursor = connection.cursor(cursor_factory=ext.DictCursor)
        cursor.execute(sql, values)
        connection.commit()
        results = cursor.fetchall()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return results
