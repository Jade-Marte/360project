from sqlite3.dbapi2 import Cursor
from flask import Flask, request, render_template, session, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

@app.route('/', methods=("POST", "GET"))
def home():
    return render_template('home.html')
@app.route('/Signin',methods=("POST","GET"))
def Signin():
    return render_template('signin.html')
def get_db():
    # file = open('schema.sql')
    # sql_code = file.read()
    # conn = mysql.connect("schema.db")
    # cursor = conn.cursor()
    # cursor.executescript(sql_code)
    conn = mysql.connection.cursor()
    conn.execute(''' SELECT employee,sessions FROM mysql.employee''')
    rv = conn.fetchall()
    return str(rv)
if __name__ == '__main__':
    conn = get_db()
    app.run(debug=True)
    