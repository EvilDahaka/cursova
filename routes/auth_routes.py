from flask import Blueprint, render_template, request, redirect, session
from database.db import get_db_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            session['user'] = username
            return redirect('/')
        else:
            return "Неправильний логін або пароль"

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')