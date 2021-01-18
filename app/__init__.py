import os
import sqlite3
import logging

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

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/products')
    def products():
        return render_template('products.html')

    if not os.path.exists('docs'):
        os.makedirs('docs')
    if not os.path.exists('docs/only_for_administration'):
        os.makedirs('docs/only_for_administration')

    logging.basicConfig(filename='./docs/only_for_administration/log_file.log', level=logging.DEBUG)

    # Add blueprints here
    from app.views import login
    from app.views import database
    from app.views import product
    from app.views import shopping_cart
    from app.views import profile
    from app.views import files

    app.register_blueprint(login.mod)
    app.register_blueprint(database.mod)
    app.register_blueprint(product.mod)
    app.register_blueprint(shopping_cart.mod)
    app.register_blueprint(profile.mod)
    app.register_blueprint(files.mod)


    db.init_app(app)

    return app
