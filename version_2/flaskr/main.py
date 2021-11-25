from sqlite3.dbapi2 import Cursor
from flask import Flask, request, render_template, session, redirect
import sqlite3

app = Flask(__name__)


@app.route('/', methods=("POST", "GET"))
def home():
    return "Hello World"
def get_db():
    file = open('schema.sql')
    sql_code = file.read()
    conn = sqlite3.connect("orsomething.db")
    cursor = conn.cursor()
    cursor.executescript(sql_code)
    return conn
if __name__ == '__main__':
    conn = get_db()
    app.run(host='0.0.0.0')
    