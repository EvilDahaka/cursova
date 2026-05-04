from flask import Blueprint, render_template, request, redirect, session
from services.item_service import ItemService
from services.category_service import CategoryService
from utils.decorators import login_required

# Створюємо Blueprint для товарів
item_bp = Blueprint('item', __name__)

# Створюємо екземпляри сервісів (об'єктний підхід)
item_service = ItemService()
category_service = CategoryService()


# Головна сторінка — список товарів користувача
@item_bp.route('/')
@login_required
def index():
    # Отримуємо всі товари поточного користувача
    items = item_service.get_by_user(session['user_id'])
    return render_template('items.html', items=items)


# Додавання товару
@item_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_item():
    if request.method == 'POST':
        # Створюємо новий товар
        result = item_service.create(request.form, session['user_id'])

        if not result:
            return "Помилка при додаванні товару"

        return redirect('/')

    # Отримуємо категорії для форми
    categories = category_service.get_all()
    return render_template('add_item.html', categories=categories)


# Видалення товару
@item_bp.route('/delete/<int:id>')
@login_required
def delete_item(id):
    # Видаляємо товар
    result = item_service.delete(id)

    if not result:
        return "Помилка при видаленні товару"

    return redirect('/')


# Редагування товару
@item_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_item(id):
    if request.method == 'POST':
        # Оновлюємо товар
        result = item_service.update(id, request.form)

        if not result:
            return "Помилка при оновленні товару"

        return redirect('/')

    # Отримуємо товар та категорії для форми
    item = item_service.get_by_id(id)
    categories = category_service.get_all()

    return render_template('edit_item.html', item=item, categories=categories)


# Пошук товарів
@item_bp.route('/search')
@login_required
def search():
    query = request.args.get('q', '')

    # Виконуємо пошук
    items = item_service.search(query, session['user_id'])

    return render_template('items.html', items=items)