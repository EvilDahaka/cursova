from functools import wraps
from flask import session, redirect

# Перевірка: користувач авторизований
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return wrapper


# Перевірка: користувач є адміністратором
def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('is_admin'):
            return "Доступ заборонено"
        return f(*args, **kwargs)
    return wrapper