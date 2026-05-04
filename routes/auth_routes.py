from flask import Blueprint, render_template, request, redirect, session
from services.user_service import UserService

# Створюємо Blueprint для авторизації
auth_bp = Blueprint('auth', __name__)

# Створюємо екземпляр сервісу (об'єктний підхід)
user_service = UserService()


# Логін користувача
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Отримуємо дані з форми
        username = request.form['username']
        password = request.form['password']

        # Виконуємо авторизацію через сервіс
        user_obj = user_service.login(username, password)

        if user_obj:
            # Зберігаємо дані користувача в сесії
            session['user'] = user_obj.username
            session['user_id'] = user_obj.id
            session['is_admin'] = user_obj.is_admin_user()

            return redirect('/')
        else:
            return render_template('login.html', error="Невірний логін або пароль")

    return render_template('login.html')


# Вихід з системи
@auth_bp.route('/logout')
def logout():
    # Очищення сесії
    session.clear()
    return redirect('/login')