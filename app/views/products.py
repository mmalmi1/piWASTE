from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response, jsonify
from app import db

mod = Blueprint('products', __name__)

@mod.route('/products')
def products():
    return render_template('products.html')

@mod.route('/products/search=', methods=['GET'])
@mod.route('/products/search=<string:name>', methods=['GET'])
def search(name=None):
    if name == None:
        command = f'SELECT product_id, name, price, description, image, stock FROM products WHERE visible = 1'
    else:    
        command = f'SELECT product_id, name, price, description, image, stock FROM products WHERE name LIKE "%{name}%" AND visible = 1'
    entrys = db.get_from_db(command)
    payload = []

    for i in entrys:
        payload.append({'product_id': i[0], 'name': i[1], 'price': i[2], 'description': i[3], 'image': i[4], 'stock': i[5]})
    return jsonify(payload)