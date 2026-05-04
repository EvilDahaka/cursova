from flask import Blueprint, render_template, request, redirect, session
from database.db import get_db_connection
from models.user import User, AdminUser

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            # 🔥 правильні відступи тут
            if user['is_admin']:
                user_obj = AdminUser(user['id'], user['username'])
            else:
                user_obj = User(user['id'], user['username'], False)

            session['user'] = user_obj.username
            session['user_id'] = user_obj.id
            session['is_admin'] = user_obj.is_admin_user()

            return redirect('/')
        else:
            return render_template('login.html', error="Невірний логін або пароль")

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')