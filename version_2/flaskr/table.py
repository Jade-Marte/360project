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