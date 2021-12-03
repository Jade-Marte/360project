from sqlite3.dbapi2 import Cursor
from flask import Flask, request, render_template, session, redirect, sessions,url_for
import mysql.connector
import json
app = Flask(__name__)
app.secret_key = 'paystub'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ajbs1900",
  database="paystub"
)
mycursor = mydb.cursor()

@app.route('/home', methods=("POST", "GET"))
@app.route('/', methods=("POST", "GET"))
def home():
    mycursor.execute("Select username,password,type,employee_id, manager_id From Employee")
    users = [dict((mycursor.description[i][0],value)\
                for i,value in enumerate(row)) for row in mycursor.fetchall()]
    # print(users)
    if request.method == 'POST':
        session.pop('user_id',None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x['username'] == username][0]
        if user and user['password'] == password:
            session['user_id'] = user['employee_id']
            session['manager_id'] = user['manager_id']
            if user['type'] == 'employee':
                print('employee logged in')
                print(user['employee_id'])
                return redirect('/employee')
            else:
                print('manager logged in')
                return redirect('/manager')
    
    return render_template('home.html', users=users)

@app.route('/test')
def test():
    query = querydb("select * from employee")
    query2 = querydb("select * from sessions")
    data = {'employee': query,'sessions': query2}
    return json.dumps(data)


@app.route('/Signup',methods=("POST","GET"))
def Signin():
    print('checking')
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        type = request.form['type']
        pay = request.form['pay_rate']
        department = request.form['department']

        mycursor.excute("""insert into employee"
                    "values (%s,%s,%s,%s,%s,%s,%s,%s)""", 
                    None,username,password,None,type,name,department,pay)
        mycursor.commit()   
        print('inserted')
    # return render_template('signin.html',users = users)
    return render_template('signup.html')



@app.route('/employee')
def employee():
    employee_id = session['user_id']
    data = querydb(f"select * from sessions where employee_id = {employee_id}")
    # print(data)
    return render_template('employee.html',data=data)


@app.route('/manager')
def manager():
    manager_id = session['manager_id']
    employee_data = querydb(f"select * from employee where manager_id = {manager_id}")
    employee_ids = [x['employee_id' ]for x in employee_data]
    # get the indivdual manager from employee_data
    manager_data = get_manager(employee_data)
    data = {'manager_name':manager_data['name'],
            'department': manager_data['department'],
            'employee': employee_data}
    return render_template('manager.html',data=data)
@app.route('/get_all_employee')
def get_employees():
    mycursor.execute("Select * FROM Employee")
    r = [dict((mycursor.description[i][0], value)
               for i, value in enumerate(row)) for row in mycursor.fetchall()]
    # mycursor.connection.close()
    return (r)

@app.route('/sessions/<employee_id>')
def get_sessions(employee_id):
    session_data = querydb(f"select * from sessions where employee_id = {employee_id}")
    for session in session_data:
        session['date'] = session['date'].strftime('%Y/%m/%d')
        # future improvement have time be am/pm
        session['time_in'] = str(session['time_in'])
        session['time_out'] = str(session['time_out'])
    return json.dumps(session_data)


# get the indivdual manager from employee_data
def get_manager(employee_data):
    for employee in employee_data:
        if employee['type'] == 'manager':
            return employee

    
def querydb(sql):
    mycursor.execute(sql)
    r = [dict((mycursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in mycursor.fetchall()]
    return (r)

if __name__ == '__main__':
    # home()
    # get_employees()
    app.run(debug=True)
    