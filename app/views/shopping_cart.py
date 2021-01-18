from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response, jsonify, json
import time
from app import db

mod = Blueprint('shopping_cart', __name__)

@mod.route('/shopping_cart', methods=['GET', 'POST'])
def shopping_cart():
    """ 
    Shopping cart view
    """

    if request.method == 'GET':
        return render_template('cart.html')

    if request.method == 'POST':
        if request.cookies.get('logged_in') == "True":
            product_ids = eval(request.cookies.get('shopping_cart', '{}')) #list of product ids, get product ids from cookie
            shopping_cart = dict()
            user_id = request.cookies.get('user_id')
            
            cart = {}
            for pid, amount in product_ids.items():
                # Ignore items that have 0 amount
                if amount != 0:
                    command = f'SELECT * FROM products WHERE product_id = {pid}'
                    prod = db.get_from_db(command)
                    prod = prod.fetchall()[0]
                    cart[prod["name"]] = [amount, round(prod["price"]*amount, 2)]
            cart = str(cart)
            t = time.asctime()
            command = f'INSERT INTO purchase_history (user_id, shopping_cart, timestamp) VALUES ("{ user_id }", "{ cart }", "{ t }")'
            print(command)
            if db.push_into_db(command):
                resp = make_response(redirect(url_for('shopping_cart.shopping_cart')))
                # Reset shopping cart
                resp.delete_cookie('shopping_cart')
            else: 
                resp = make_response("Cannot make purchase!")

        else:
            resp = make_response("Please login to make a purchase")

        return resp

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
            'amount': amount,
            'image': data['image']
        }
    print("shopping cart:", shopping_cart)
    return make_response(shopping_cart)
