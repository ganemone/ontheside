from app_factory import db
from models import User
from forms import RegistrationForm, LoginForm


def load_user(user_id):
    return User.query.filter_by(id=user_id)


def register(request):
    form = RegistrationForm.from_json(request.form)
    if request.method == 'POST' and form.validate():
        user = User(
            name=form.name,
            username=form.username,
            password=form.password,
            email=form.email
        )
        db.session.add(user)
        db.session.commit()


def login(request):
    form = LoginForm.from_json(request.form)
    if request.method == 'POST' and form.validate():
        # Do login stuff here
