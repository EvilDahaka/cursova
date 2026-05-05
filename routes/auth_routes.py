from flask import Blueprint, render_template, request, redirect, session, flash
from services.user_service import UserService

auth_bp = Blueprint('auth', __name__)

user_service = UserService()


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('_flashes', None)

        username = request.form.get('username')
        password = request.form.get('password')

        user_obj = user_service.login(username, password)

        if user_obj:
            session['user'] = user_obj.username
            session['user_id'] = user_obj.id
            session['is_admin'] = user_obj.is_admin

            flash("Вхід виконано успішно", "success")
            return redirect('/')
        else:
            flash("Невірний логін або пароль", "danger")
            return render_template('login.html')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Ви вийшли з системи", "info")
    return redirect('/login')