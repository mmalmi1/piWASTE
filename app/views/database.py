from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response, jsonify

mod = Blueprint('database', __name__)

from app import db

@mod.route("/admin/create_product")
def create_product():
    """
    Creates a new product. Currently not possible to set product image, uses assets/placeholder.png
    Name, price, description and stock need to be provided
    Visible is optional (defaults to 1)
    example: /admin/create_product?name=<name>&price=<price>&description=<description>&stock=<stock>

    """
    vals = request.args

    # Check access level from database
    user_id = eval(request.cookies.get('user_id'))
    command = f'SELECT access_level FROM users WHERE user_id="{user_id}"'
    user = db.get_from_db(command).fetchone()
    access_level = user["access_level"]

    if access_level < 2:
        return Response("Unauthorized", 403)
    command = f'INSERT INTO products (name, price, description, stock, image, visible) VALUES ("{vals.get("name")}", "{vals.get("price")}", "{vals.get("description")}", "{vals.get("stock")}", "assets/placeholder.png", "{vals.get("visible", 1)}")'
    if db.push_into_db(command):
        return "Created product"
    return "Failed to create product"