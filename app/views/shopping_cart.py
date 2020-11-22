from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response
from app import db

mod = Blueprint('shopping_cart', __name__)

@mod.route('/shopping_cart', methods=['GET', 'POST'])
def shopping_cart():
    """ 
    Shopping cart view
    """

    return render_template('cart.html')

@mod.route('/get_shopping_cart', methods=['GET', 'POST'])
def get_shopping_cart():
    """ 
    Get shopping cart
    TODO: Add remove product from cart
    """
    product_ids = eval(request.cookies.get('shopping_cart', '{}')) #list of product ids, get product ids from cookie
    shopping_cart = dict()
    for pid, amount in product_ids.items():
        command = f'SELECT * FROM products WHERE product_id = {pid}'
        data = db.get_from_db(command).fetchone()
        shopping_cart[pid] = {
            'name': data['name'],
            'price': data['price'],
            'description': data['description'],
            'amount': amount
        }
    print("shopping cart:", shopping_cart)
    return make_response(shopping_cart)
