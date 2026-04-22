from flask import Blueprint, render_template, request, redirect, session
from database.db import get_db_connection

item_bp = Blueprint('item', __name__)

@item_bp.route('/')
def index():
    if 'user' not in session:
        return redirect('/login')

    conn = get_db_connection()
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()

    return render_template('items.html', items=items)


@item_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        year = request.form['year']
        price = request.form['price']
        condition = request.form['condition']

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO items (name, category, year, price, condition) VALUES (?, ?, ?, ?, ?)",
            (name, category, year, price, condition)
        )
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('add_item.html')


@item_bp.route('/delete/<int:id>')
def delete_item(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM items WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@item_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    conn = get_db_connection()

    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        year = request.form['year']
        price = request.form['price']
        condition = request.form['condition']

        conn.execute('''
            UPDATE items
            SET name=?, category=?, year=?, price=?, condition=?
            WHERE id=?
        ''', (name, category, year, price, condition, id))

        conn.commit()
        conn.close()

        return redirect('/')

    item = conn.execute("SELECT * FROM items WHERE id = ?", (id,)).fetchone()
    conn.close()

    return render_template('edit_item.html', item=item)

@item_bp.route('/search')
def search():
    query = request.args.get('q')

    conn = get_db_connection()
    items = conn.execute(
        "SELECT * FROM items WHERE name LIKE ?",
        ('%' + query + '%',)
    ).fetchall()
    conn.close()

    return render_template('items.html', items=items)