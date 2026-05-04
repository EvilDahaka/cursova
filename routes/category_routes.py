from flask import Blueprint, render_template, request, redirect, session
from services.category_service import CategoryService

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['GET', 'POST'])
def categories():

    if 'user' not in session:
        return redirect('/login')

    if not session.get('is_admin'):
        return "Доступ заборонено"

    if request.method == 'POST':
        name = request.form['name']
        CategoryService.create(name)
        return redirect('/categories')

    categories = CategoryService.get_all()
    return render_template('categories.html', categories=categories)


@category_bp.route('/categories/delete/<int:id>')
def delete_category(id):
    if not session.get('is_admin'):
        return "Доступ заборонено"

    CategoryService.delete(id)
    return redirect('/categories')