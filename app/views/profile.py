from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response
from app import db

mod = Blueprint('profile', __name__)

@mod.route('/profile', methods=['GET'])
def profile():
    """
    User profile view
    """
    user_id = eval(request.cookies.get('user_id'))
    command = f'SELECT username, name, email, phone, address FROM users WHERE user_id = {user_id}'
    profile = db.get_from_db(command).fetchall()[0]
    return make_response(
        render_template('profile.html', user_id=user_id, username=profile['username'],
                        name=profile['name'], email=profile['email'],
                        phone=profile['phone'], address=profile['address']))