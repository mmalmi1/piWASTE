from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response, jsonify, json
import time
from app import db

mod = Blueprint('register', __name__)

@mod.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register Profile View
    """
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone = request.form['phone']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        # passwordRepeat = request.form['passwordRepeat']

        command = f'INSERT INTO users (username, name, email, phone, address, password, access_level) VALUES ("{username}", "{name}", "{email}", "{phone}", "{address}", "{password}", 1)'


        if db.push_into_db(command):
            # Inserts new user, if username is not in use
            # Directs to profile page as new user
            return make_response(redirect(url_for('login.login')))
        else:
            return make_response(render_template('register.html'))

    else:
        # Add here exception for already logged in.
        return make_response(render_template('register.html'))

