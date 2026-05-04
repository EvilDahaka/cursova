from flask import Blueprint, render_template, request, redirect, session
from services.item_service import ItemService
from services.category_service import CategoryService

item_bp = Blueprint('item', __name__)

@item_bp.route('/')
def index():
    if 'user' not in session:
        return redirect('/login')

    items = ItemService.get_by_user(session['user_id'])
    return render_template('items.html', items=items)


@item_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        if not request.form['name']:
            return "Помилка: введіть назву"

        if not request.form['price']:
            return "Помилка: введіть ціну"

        ItemService.create(request.form, session['user_id'])
        return redirect('/')

    categories = CategoryService.get_all()
    return render_template('add_item.html', categories=categories)


@item_bp.route('/delete/<int:id>')
def delete_item(id):
    ItemService.delete(id)
    return redirect('/')

@item_bp.route('/search')
def search():
    if 'user' not in session:
        return redirect('/login')

    query = request.args.get('q', '')
    items = ItemService.search(query, session['user_id'])
    return render_template('items.html', items=items)

@item_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    if 'user' not in session:
        return redirect('/login')

    item = ItemService.get_by_id(id)

    if request.method == 'POST':
        ItemService.update(id, request.form)
        return redirect('/')

    categories = CategoryService.get_all()
    return render_template('edit_item.html', item=item, categories=categories)