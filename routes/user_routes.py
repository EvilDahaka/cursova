from flask import Blueprint, render_template, request, redirect, session
from services.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET', 'POST'])
def users():

    if 'user' not in session:
        return redirect('/login')

    if not session.get('is_admin'):
        return "Доступ заборонено"

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        UserService.create(username, password)
        return redirect('/users')

    users = UserService.get_all()
    return render_template('users.html', users=users)


@user_bp.route('/users/delete/<int:id>')
def delete_user(id):
    if not session.get('is_admin'):
        return "Доступ заборонено"

    UserService.delete(id)
    return redirect('/users')