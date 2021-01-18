from flask import Blueprint, render_template, url_for, request, redirect, Response, make_response, jsonify, json
import time
from app import db

mod = Blueprint('profile', __name__)

@mod.route('/profile', methods=['GET'])
def profile():
    """
    User profile view
    """
    user_id = eval(request.cookies.get('user_id'))
    command = f'SELECT username, name, email, phone, address FROM users WHERE user_id = {user_id}'
    profile = db.get_from_db(command).fetchall()
    if len(profile) > 0:
        profile = profile[0]
        return make_response(
            render_template('profile.html', user_id=user_id, username=profile['username'],
                            name=profile['name'], email=profile['email'],
                            phone=profile['phone'], address=profile['address']))
    return make_response(redirect(url_for('login.login')))

@mod.route('/profile/edit', methods=['GET','POST'])
def edit():
    """
    Edit the user profile
    """
    user_id = eval(request.cookies.get('user_id'))
    if request.method == 'GET':
        command = f'SELECT name, phone, address, password FROM users WHERE user_id = {user_id}'
        profile = db.get_from_db(command).fetchall()
        if len(profile) > 0:
            profile = profile[0]
            return make_response(render_template('edit_profile.html',
                                name=profile['name'], phone=profile['phone'],
                                address=profile['address'], password=profile['password']))
        return Response("Need to log in to access profile information", 401)
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone = request.form['phone']
        password = request.form['password']
        if name:
            command = f'UPDATE users SET name = "{name}" WHERE user_id = {user_id}'
            db.push_into_db(command)
        if address:
            command = f'UPDATE users SET address = "{address}" WHERE user_id = {user_id}'
            db.push_into_db(command)
        if phone:
            command = f'UPDATE users SET phone = "{phone}" WHERE user_id = {user_id}'
            db.push_into_db(command)
        if password:
            command = f'UPDATE users SET password = "{password}" WHERE user_id = {user_id}'
            db.push_into_db(command)
        return make_response(redirect(url_for('profile.profile')))

@mod.route('/get_purchase_history/<string:userId>')
def get_from_db(userId=None):
    """
    Get user's purchase history by id, return json.
    """
    command = f'SELECT * FROM purchase_history WHERE user_id = {userId}'
    entrys = db.get_from_db(command)
    payload = []

    for i in entrys:
        payload.append({'user_id': i[0], 'shopping_cart': i[1], 'timestamp': i[2]})
    return jsonify(payload)
