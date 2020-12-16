from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response
from app import db

mod = Blueprint('login', __name__)

@mod.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login returns three cookies:
        logged_in: True/False string
        user_id: user id integer as string
    """
    error = None
    logged_in = 'False'
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
            user_id = str(user["user_id"])
            resp = make_response(redirect(url_for('index')))
    resp.set_cookie('logged_in', logged_in)
    resp.set_cookie('user_id', user_id)
    return resp

@mod.route('/logout')
def logout():
    """
    Logs out the current user by resetting the cookie values to default
    """
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('logged_in', 'False')
    resp.set_cookie('user_id', '0')
    return resp
