from flask import Blueprint, render_template, request, redirect, session
from services.item_service import ItemService

item_bp = Blueprint('item', __name__)

@item_bp.route('/')
def index():
    if 'user' not in session:
        return redirect('/login')

    items = ItemService.get_all()
    return render_template('items.html', items=items)


@item_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        ItemService.create(request.form)
        return redirect('/')

    return render_template('add_item.html')


@item_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    if request.method == 'POST':
        ItemService.update(id, request.form)
        return redirect('/')

    item = ItemService.get_by_id(id)
    return render_template('edit_item.html', item=item)


@item_bp.route('/delete/<int:id>')
def delete_item(id):
    ItemService.delete(id)
    return redirect('/')


@item_bp.route('/search')
def search():
    query = request.args.get('q')
    items = ItemService.search(query)
    return render_template('items.html', items=items)