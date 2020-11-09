from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response
from app import db

mod = Blueprint('shopping_cart', __name__)

@mod.route('/shopping_cart', methods=['GET', 'POST'])
def shopping_cart():
    """ 
    Shopping cart view
    TODO: Create HTML for shopping cart
          Add remove product from cart
    """
    
    productIds = request.cookies.get('shopping_cart') #list of product ids, get product ids from cookie

    command = f'SELECT * FROM products WHERE product_id = {productIds}'
    shopping_cart = db.get_from_db(command)

    print("shopping cart:", shopping_cart)

    resp = make_response(render_template('shopping_cart.html'))
    return resp
