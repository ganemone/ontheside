from flask import Response

from flask_login import login_user
from server.models import User
from server.login_manager import login_manager


@login_manager.user_loader
def load_user(user_id):
    """Returns a user from the database based on their id"""
    return User.query.filter_by(id=user_id).first()


def handle_basic_auth(request):
    auth = request.authorization
    if not auth:
        return None
    return User.query.filter_by(
        username=auth.username,
        password=auth.password
    ).first()


def login(request):
    """Handle a login request from a user."""
    user = handle_basic_auth(request)
    if user:
        login_user(user, remember=True)
        return 'OK'
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})
