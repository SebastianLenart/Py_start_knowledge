from flask import Response
from db import get_connection
from json import dumps


def index():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, first_name, last_name FROM authors")
    return Response(dumps(cursor.fetchall()), mimetype="application/json") # ladniejsza postac jsona

def add():
    return "add"

def delete():
    return "delete"