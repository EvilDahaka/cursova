from flask import Blueprint, render_template, request, redirect, session
from services.user_service import UserService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = UserService.login(
            request.form['username'],
            request.form['password']
        )

        if user:
            session['user'] = user['username']
            return redirect('/')
        else:
            return render_template('login.html', error="Невірний логін або пароль")

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')