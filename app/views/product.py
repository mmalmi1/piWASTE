from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response
from app import db

mod = Blueprint('product', __name__)

@mod.route('/product/<int:productId>')
def product(productId=None):
    '''
    Product view.
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        price REAL NOT NULL,
        description TEXT NOT NULL,
        image TEXT,
        stock INTEGER DEFAULT 0
    );
    '''

    command = f'SELECT * FROM products WHERE product_id = {productId}'
    prod = db.get_from_db(command)
    prod = prod.fetchall()[0]
    img = """ "{{url_for('static', filename='""" + prod["image"] + """')}}" """
    print(img)
    resp = make_response(render_template('product.html', product_id=prod["product_id"], name=prod["name"],
                                        price=prod["price"], description=prod["description"],
                                        image=img, stock=prod["stock"]))
    return resp
