from flask import Blueprint, render_template, request, redirect, session
from services.item_service import ItemService
from services.category_service import CategoryService
from utils.decorators import login_required

item_bp = Blueprint('item', __name__)

# Головна сторінка — список товарів користувача
@item_bp.route('/')
@login_required
def index():
    items = ItemService.get_by_user(session['user_id'])
    return render_template('items.html', items=items)


# Додавання товару
@item_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_item():
    if request.method == 'POST':
        ItemService.create(request.form, session['user_id'])
        return redirect('/')

    categories = CategoryService.get_all()
    return render_template('add_item.html', categories=categories)


# Видалення товару
@item_bp.route('/delete/<int:id>')
@login_required
def delete_item(id):
    ItemService.delete(id)
    return redirect('/')


# Редагування товару
@item_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_item(id):
    if request.method == 'POST':
        ItemService.update(id, request.form)
        return redirect('/')

    item = ItemService.get_by_id(id)
    categories = CategoryService.get_all()
    return render_template('edit_item.html', item=item, categories=categories)


# Пошук товарів
@item_bp.route('/search')
@login_required
def search():
    query = request.args.get('q', '')
    items = ItemService.search(query, session['user_id'])
    return render_template('items.html', items=items)