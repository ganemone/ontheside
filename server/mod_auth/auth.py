from app_factory.create_app import db
from models import User
from forms import RegistrationForm, LoginForm


def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


def login(request):
    form = LoginForm.from_json(request.form)
    if request.method == 'POST' and form.validate():
        return True
