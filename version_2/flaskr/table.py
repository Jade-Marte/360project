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
        " FROM   p JOIN user u ON p.employee_id = u.id"
        " ORDER BY session_time DESC"
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
                'INSERT INTO entry(client_name, session_time, employee_id)'
                'VALUES (?,?,?)',
                (client_name,session,employee_name,g.user['id'])
            )
            db.commit()
            return redirect(url_for('table.index'))
    return render_template('payroll/create.html')

def get_post(id,check_employee=True):
    entry = get_db().execute(
        "SELECT id,client_name,payment,session_time,employee_id,username"
        "FROM entry p JOIN user u ON p.employee_id = u.id"
        "WHERE id = ?",
        (id,)
    ).fetchone()

    if entry is None:
        abort(404,f"Entry id {id} doesn't exist.")
    if check_employee and entry['employee_id'] != g.user['id']:
        abort(403)
    return entry

@bp.route('/<int:id>/update',methods=('GET','POST'))
@login_required
def update(id):
    entry = get_post(id)

    if request.method =='POST':
        client_name = request.form['client_name']
        employee_name = request.form['employee_name']
        session_time = request.form['session_time']
        error = None
        if not client_name:
            error = 'Client name is required.'
        if error is not None:
            flash(error)
        else:
            db =get_db()
            db.execute(
                'UPDATE entry Set client_name = ?, session_time = ?, employee_name = ?'
                "where id = ?",
                (client_name,session_time,id,employee_name)
            )
            db.commit()
            return redirect(url_for('table.index'))

    return render_template('payroll/update.html',entry=entry)

@bp.route('/<int:id>/delete', methods=("POST",))
@login_required
def delete(id):
    get_post(id)
    db=get_db()
    db.execute('DELETE FROM post WHERE id = ?',(id,))
    db.commit()
    return redirect(url_for('table.index'))