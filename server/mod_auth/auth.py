from flask import Response
from flask.ext.login import login_user
from server.app_factory import login_manager
from server.models import User


@login_manager.user_loader
def load_user(user_id):
    """Returns a user from the database based on their id"""
    return User.query.filter_by(id=user_id).first()


def login(request):
    """Handle a login request from a user."""
    user = User.query.filter_by(
        username=request.authorization.username,
        password=request.authorization.password
    ).first()
    if user is not None:
        login_user(user)
        return 'OK'
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})
