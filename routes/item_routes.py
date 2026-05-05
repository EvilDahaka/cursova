from flask import Blueprint, render_template, request, redirect, session, flash
from services.item_service import ItemService
from services.category_service import CategoryService
from utils.decorators import login_required

item_bp = Blueprint('item', __name__)

item_service = ItemService()
category_service = CategoryService()


@item_bp.route('/')
@login_required
def index():
    query = request.args.get('q', '').strip()

    if query:
        items = item_service.search(query, session['user_id'])
    else:
        items = item_service.get_by_user(session['user_id'])

    return render_template('items.html', items=items)


@item_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_item():
    if request.method == 'POST':
        result = item_service.create(request.form, session['user_id'])

        if result:
            flash("Товар додано", "success")
        else:
            flash("Помилка при додаванні", "danger")

        return redirect('/')

    categories = category_service.get_all()
    return render_template('add_item.html', categories=categories)


@item_bp.route('/delete/<int:id>')
@login_required
def delete_item(id):
    result = item_service.delete(id)

    if result:
        flash("Товар видалено", "info")
    else:
        flash("Помилка при видаленні", "danger")

    return redirect('/')


@item_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_item(id):
    if request.method == 'POST':
        result = item_service.update(id, request.form)

        if result:
            flash("Товар оновлено", "success")
        else:
            flash("Помилка при оновленні", "danger")

        return redirect('/')

    item = item_service.get_by_id(id)
    categories = category_service.get_all()

    return render_template('edit_item.html', item=item, categories=categories)