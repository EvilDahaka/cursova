from flask import Blueprint, render_template, request, redirect
from services.category_service import CategoryService
from utils.decorators import login_required, admin_required

category_bp = Blueprint('category', __name__)

# Список категорій
@category_bp.route('/categories')
@login_required
@admin_required
def categories():
    categories = CategoryService.get_all()
    return render_template('categories.html', categories=categories)

# Додавання категорії
@category_bp.route('/categories/add', methods=['POST'])
@login_required
@admin_required
def add_category():
    name = request.form['name']
    result = CategoryService.create(name)

    if not result:
        return "Помилка при створенні категорії"

    return redirect('/categories')

# Видалення категорії
@category_bp.route('/categories/delete/<int:id>')
@login_required
@admin_required
def delete_category(id):
    result = CategoryService.delete(id)

    if not result:
        return "Не вдалося видалити категорію"

    return redirect('/categories')