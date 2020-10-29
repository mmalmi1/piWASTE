import os
import sqlite3

from flask import Flask, render_template, url_for, request, redirect, session, jsonify, Response, make_response



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
    
    @app.route('/all_products')
    def get_all_products_from_db():
        command = f"SELECT * FROM products"
        products = db.get_from_db(command)
        payload = []
        for result in products:
            payload.append({'id': result[0], 'name': result[1], 'price': result[2], 'description': result[3], 'image': result[4], 'stock': result[5]})
        return jsonify(payload)

    @app.route('/')
    def index():
        return render_template('index.html')
        
    @app.route('/products')
    def products():
        return render_template('products.html')
        
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """
        Login returns three cookies:
            logged_in: True/False string
            access_level: user access level integer as string
            user_id: user id integer as string
        """
        error = None
        logged_in = 'False'
        access_level = '0'
        user_id = '0'
        resp = make_response(render_template('login.html'))
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            command = f'SELECT user_id, access_level FROM users WHERE username="{username}" AND password="{password}"'

            # If multiple results are returned by the db query, will pick the first one.
            user = db.get_from_db(command).fetchone()
            if user is None:
                error = 'Invalid Credentials. Please try again.'
                resp = make_response(render_template('login.html', error=error))
            else:
                logged_in = 'True'
                access_level = str(user["access_level"])
                user_id = str(user["user_id"])
                resp = make_response(redirect(url_for('index')))
        resp.set_cookie('logged_in', logged_in)
        resp.set_cookie('access_level', access_level)
        resp.set_cookie('user_id', user_id)
        return resp

    @app.route('/logout')
    def logout():
        """
        Logs out the current user by resetting the cookie values to default
        """
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('logged_in', 'False')
        resp.set_cookie('access_level', "0")
        resp.set_cookie('user_id', '0')
        return resp

    @app.route('/secret')
    def secret():
        """
        A simple example to check user is logged in
        """
        logged_in = request.cookies.get('logged_in')
        if logged_in != 'True':
            return Response("It's a secret", 401)
        return "Congratulations, you found the secret"

    @app.route('/admin')
    def admin():
        """
        A simple example to check user access level
        """
        access_level = int(request.cookies.get('access_level'))
        if access_level < 1:
            return Response("Unauthorized", 401)
        return "Welcome!"

    db.init_app(app)

    return app
