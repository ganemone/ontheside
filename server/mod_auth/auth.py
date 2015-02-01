from models import User
from forms import LoginForm


def load_user(user_id):
    """Returns a user from the database based on their id"""
    return User.query.filter_by(id=user_id).first()


def login(request):
    """Handle a login request from a user."""
    form = LoginForm.from_json(request.form)
    if request.method == 'POST' and form.validate():
        return True
