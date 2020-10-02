import os

from flask import Flask, render_template


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
    @app.route('/get_all_product_ids')
    def get_from_db():
        command = f"SELECT id FROM product"
        ids = db.get_from_db(command)
        resp = ''
        for i in ids:
            resp += str(i['id']) + ":"
        return resp

    @app.route('/push/<string:name>/<float:price>/<string:desc>')
    def push_into_db(name=None, price=None, desc=None):
        command = f'INSERT INTO product (name, price, description) VALUES ("{name}", "{price}", "{desc}")'
        db.push_into_db(command)
        return "OK"

    @app.route('/')
    def index():
        return render_template('index.html')

    db.init_app(app)

    return app