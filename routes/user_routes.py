from flask import Blueprint, render_template, request, redirect
from services.user_service import UserService
from utils.decorators import login_required, admin_required

user_bp = Blueprint('user', __name__)

# Список користувачів (тільки для адміністратора)
@user_bp.route('/users')
@login_required
@admin_required
def users():
    users = UserService.get_all()
    return render_template('users.html', users=users)

# Створення нового користувача
@user_bp.route('/users/add', methods=['POST'])
@login_required
@admin_required
def add_user():
    username = request.form['username']
    password = request.form['password']
    is_admin = int(request.form.get('is_admin', 0))

    result = UserService.create(username, password, is_admin)

    if not result:
        return "Помилка при створенні користувача"

    return redirect('/users')

# Видалення користувача
@user_bp.route('/users/delete/<int:id>')
@login_required
@admin_required
def delete_user(id):
    result = UserService.delete(id)

    if not result:
        return "Помилка при видаленні користувача"

    return redirect('/users')