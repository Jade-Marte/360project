from sqlite3.dbapi2 import Cursor
from flask import Flask, request, render_template, session, redirect
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ajbs1900",
  database="paystub"
)
print(mydb)

@app.route('/', methods=("POST", "GET"))
def home():
    data = {'name': 'Dummy1','date': 'today','status':'closed'}
    return render_template('home.html', data=data)

@app.route('/Signin',methods=("POST","GET"))
def Signin():
    return render_template('signin.html')

@app.route('/get_all_employee')
def get_employees():
    mycursor = mydb.cursor()
    mycursor.execute("Select * FROM Employee")
    r = [dict((mycursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in mycursor.fetchall()]
    # mycursor.connection.close()
    return (r[0])

if __name__ == '__main__':
    get_employees()
    app.run(debug=True)
    