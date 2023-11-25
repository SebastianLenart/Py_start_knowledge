from psycopg2 import connect
from flask import g


def init_app(app):
    app.teardown_appcontext(close_connection)


def get_connection():
    print("ASASASAS")
    print(g)
    if 'connection' in g:
        g.connection = connect(dbname="app", user="app", password="admin123", host="db")
    return g.connection


def close_connection():
    connection = g.pop("connection", None)
    if connection is not None:
        connection.close()
