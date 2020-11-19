from flask import request, Blueprint

mod = Blueprint('crim_demo', __name__)

from app import db

@mod.route('/secret')
def secret():
    """
    A simple example to check user is logged in
    
    NOTE: eval is evil
    """
    logged_in = request.cookies.get('logged_in')
    if not eval(logged_in):
        return Response("It's a secret", 401)
    return "Congratulations, you found the secret"

@mod.route('/admin')
def admin():
    """
    A simple example to check user access level
    """
    access_level = int(request.cookies.get('access_level'))
    if access_level < 2:
        return Response("Unauthorized", 401)
    return "Welcome!"
