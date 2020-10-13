import os

from flask import Flask, render_template, url_for


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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

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

    # create entry to products table
    @app.route('/push_products/<string:name>/<float:price>/<string:desc>')
    def push_product(name=None, price=None, desc=None):
        command = f'INSERT INTO products (name, price, description) VALUES ("{name}", "{price}", "{desc}")'
        db.push_into_db(command)
        return "OK"

    # create entry to users table
    @app.route('/push_users/<string:username>/<string:password>/<int:access_level>')
    def push_user(username=None, password=None, access_level=None):
        command = f'INSERT INTO users (username, password, access_level) VALUES ("{username}", "{password}", "{access_level}")'
        db.push_into_db(command)
        return "OK"

    # create entry to reviews table
    @app.route('/push_reviews/<string:text>/<int:user_id>/<int:product_id>')
    def push_review(text=None, user_id=None, product_id=None):
        command = f'INSERT INTO reviews (text, user_id, product_id) VALUES ("{text}", "{user_id}", "{product_id}")'
        db.push_into_db(command)
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