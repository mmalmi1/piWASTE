from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response
from app import db

mod = Blueprint('product', __name__)

@mod.route('/product/<int:productId>')
def product(productId=None):


    command = f'SELECT * FROM products WHERE product_id = {productId}'
    prod = db.get_from_db(command)
    print(tuple(prod))
    resp = make_response(render_template('product.html'))
    return resp