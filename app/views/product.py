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

@mod.route('/product/<int:productId>/addToCart')
def addToCart(productId=None):
    """
    Add product to shopping cart by using cookies:
        shopping_cart: List of product ids
    
    Since cookies apparently only accept strings, the list has to be converted back and forth between string and list
    by using str() to convert to string and eval() to convert back to list

    TODO: Add many items to cart at once
    """

    logged_in = request.cookies.get('logged_in') # Check if logged in by checking cookie
    
    if logged_in == 'False':
        resp = make_response(render_template('login.html')) # Go to login page or throw exception or something
    else:
        shopping_cart = eval(request.cookies.get('shopping_cart')) # get current shopping cart from cookie and convert to list

        if shopping_cart is None:
            shopping_cart = []

        shopping_cart.append(productId) # add productId to end of list

        print("Added product to cart")
        print(shopping_cart)

        resp = make_response("Set shopping cart cookie") # dont know what to put here
        resp.set_cookie('shopping_cart', str(shopping_cart)) # set cookie and set list to string

    return resp