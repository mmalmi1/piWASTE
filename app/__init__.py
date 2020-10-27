import os
import sqlite3
from flask import Flask, render_template, url_for, request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    # get all entrys in a specified database
    # prints them into the server log
    @app.route('/get_all_entrys/<string:database>')
    def get_from_db(database=None):
        command = f"SELECT * FROM {database}"
        entrys = db.get_from_db(command)
        for i in entrys:
            print(tuple(i))
        return "OK"

    # query database, example query below
    # http://127.0.0.1:5000/data?table=users&username=admin2&password=admin&access_level=1
    @app.route('/data')
    def query():
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

    @app.route('/')
    def index():
        return render_template('index.html')
        
    @app.route('/products')
    def products():
        return render_template('products.html')
        
    @app.route('/login')
    def login():
        return render_template('login.html')

    db.init_app(app)

    return app