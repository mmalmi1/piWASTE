from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response
from app import db

mod = Blueprint('product', __name__)

@mod.route('/product/<int:product_id>', methods=['GET'])
def product(product_id=None):
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

    command = f'SELECT * FROM products WHERE product_id = {product_id}'
    prod = db.get_from_db(command)
    prod = prod.fetchall()[0]

    command = f'SELECT * FROM reviews WHERE product_id = {product_id}'
    reviews = db.get_from_db(command)
    reviews = reviews.fetchall()

    resp = make_response(render_template('product.html', product_id=prod["product_id"], name=prod["name"],
                                        price=prod["price"], description=prod["description"],
                                        image=prod["image"], stock=prod["stock"], reviews=reviews))
    return resp

@mod.route('/product/<int:product_id>/submit_review', methods=['POST'])
def submit_review(product_id=None):
    '''
    Post a review for a product
    '''
    if request.cookies.get('logged_in') == "True":
        message = request.form['message']
        user_id = request.cookies.get('user_id')

        command = f'SELECT username FROM users WHERE user_id = {user_id}'
        username = db.get_from_db(command)
        username = username.fetchall()[0]
        username = username["username"]

        command = f'INSERT INTO reviews (text, username, product_id) VALUES ("{message}", "{username}", "{product_id}")'
        if db.push_into_db(command):
            resp = make_response(product(product_id))
        else:
            resp = make_response("You have already posted a review for this product!")
    else:
        resp = make_response("Please login to leave review!")

    return resp
