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
            payload.append({'id': i[0], 'name': i[1], 'price': i[2], 'description': i[3], 'image': i[4], 'stock': i[5]})
        return jsonify(payload)
    for i in entrys:
        print(tuple(i))
    return "OK"

@mod.route('/data')
def query():
    """
    query database, example query below
    http://127.0.0.1:5000/data?table=users&username=admin2&password=admin&access_level=1
    """
    table = request.args.get('table')
    if table == "products":
        command = f'INSERT INTO products (name, price, description) VALUES ("{request.args.get("name")}", "{request.args.get("price")}", "{request.args.get("description")}")'
    elif table == 'users':
        command = f'INSERT INTO users (username, password, access_level) VALUES ("{request.args.get("username")}", "{request.args.get("password")}", "{request.args.get("access_level")}")'
    elif table == 'reviews':
        command = f'INSERT INTO reviews (text, user_id, product_id) VALUES ("{request.args.get("text")}", "{request.args.get("user_id")}", "{request.args.get("product_id")}")'
    else:
        return "query failed, table not found"

    success = db.push_into_db(command)
    return "OK"