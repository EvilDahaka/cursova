from flask import Blueprint, render_template, request, redirect
from services.category_service import CategoryService
from utils.decorators import login_required, admin_required

# Створюємо Blueprint
category_bp = Blueprint('category', __name__)

# Створюємо ОДИН екземпляр сервісу (об'єктний підхід)
category_service = CategoryService()


# Сторінка категорій (тільки для адміна)
@category_bp.route('/categories')
@login_required
@admin_required
def categories():
    # Отримуємо список об'єктів Category
    categories = category_service.get_all()
    return render_template('categories.html', categories=categories)


# Додавання категорії
@category_bp.route('/categories/add', methods=['POST'])
@login_required
@admin_required
def add_category():
    name = request.form.get('name')

    try:
        result = category_service.create(name)

        if not result:
            return "Помилка при створенні категорії"

    except ValueError as e:
        # Обробка валідації (з сервісу)
        return str(e)

    return redirect('/categories')


# Видалення категорії
@category_bp.route('/categories/delete/<int:id>')
@login_required
@admin_required
def delete_category(id):
    result = category_service.delete(id)

    if not result:
        return "Не вдалося видалити категорію"

    return redirect('/categories')