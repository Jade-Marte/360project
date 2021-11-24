from flask import(
    Blueprint,flash,g,redirect,render_template,request,url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('table',__name__)

@bp.route('/')
def index():
    db = get_db()
    table = db.execute(
        "SELECT p.id, employee_id,session_time,employee_name,client_name,payment,username"
        "FROM payroll p JOIN user u ON p.employee_id = u.id"
        "ORDER BY employee_name DESC"
    ).fetchall()
    return render_template('table/index.html',table=table)

@bp.route('/create',methods=('GET','POST'))
@login_required
def create():
    if request.method =='POST':
        client_name = request.form['client_name']
        employee_name = request.form['employee_name']
        session = request.form['session_time']
        error = None

        if not client_name:
            error = 'client name is required'
        
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO entry (client_name,pay, employee_id)'
                'VALUES (?,?,?)'
                (client_name,employee_name,g.user['id'])
            )
            db.commit()
            return redirect(url_for('table.index'))
    return render_template('payroll/create.html')