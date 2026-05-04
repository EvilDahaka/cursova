from flask import Blueprint, render_template, request, redirect
from services.user_service import UserService
from utils.decorators import login_required, admin_required

# Blueprint для користувачів
user_bp = Blueprint('user', __name__)

# Створюємо об'єкт сервісу (ОБОВʼЯЗКОВО)
user_service = UserService()


# Список користувачів (тільки для адміна)
@user_bp.route('/users')
@login_required
@admin_required
def users():
    # Отримуємо всіх користувачів як об'єкти
    users = user_service.get_all()
    return render_template('users.html', users=users)


# Додавання користувача
@user_bp.route('/users/add', methods=['POST'])
@login_required
@admin_required
def add_user():
    username = request.form['username']
    password = request.form['password']
    is_admin = int(request.form.get('is_admin', 0))

    result = user_service.create(username, password, is_admin)

    if not result:
        return "Помилка при створенні користувача"

    return redirect('/users')


# Видалення користувача
@user_bp.route('/users/delete/<int:id>')
@login_required
@admin_required
def delete_user(id):
    result = user_service.delete(id)

    if not result:
        return "Помилка при видаленні користувача"

    return redirect('/users')