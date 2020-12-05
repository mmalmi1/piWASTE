from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response, jsonify

mod = Blueprint('database', __name__)

from app import db

@mod.route('/get_all_entrys/<string:database>')
def get_from_db(database=None):
    """
    get all entrys in a specified database
    prints them into the server log
    """
    command = f"SELECT * FROM {database}"
    entrys = db.get_from_db(command)
    payload = []
    if database == "products":
        for i in entrys:
            if i[-1] != 0: # Only return visible products
                payload.append({'id': i[0], 'name': i[1], 'price': i[2], 'description': i[3], 'image': i[4], 'stock': i[5]})
        return jsonify(payload)
    for i in entrys:
        print(tuple(i))
    return "OK"

@mod.route("/admin/create_product")
def create_product():
    """
    Creates a new product. Currently not possible to set product image, uses assets/placeholder.png
    Name, price, description and stock need to be provided
    Visible is optional (defaults to 1)
    example: /admin/create_product?name=<name>&price=<price>&description=<description>&stock=<stock>

    """
    vals = request.args
    access_level = eval(request.cookies.get('access_level'))
    if access_level < 2:
        return Response("Unauthorized", 403)
    command = f'INSERT INTO products (name, price, description, stock, image, visible) VALUES ("{vals.get("name")}", "{vals.get("price")}", "{vals.get("description")}", "{vals.get("stock")}", "assets/placeholder.png", "{vals.get("visible", 1)}")'
    if db.push_into_db(command):
        return "Created product"
    return "Failed to create product"