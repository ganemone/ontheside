from wtforms import Form, StringField, PasswordField, validators
from server.forms import db_match
from server.models import User


class LoginForm(Form):
    # Login name can be either username or email
    user_exists_validator = db_match(
        model=User,
        message='Invalid username/password combination',
        query_fields=['username', 'password'],
    )
    username = StringField(
        'username',
        [
            validators.Required(),
            validators.Length(min=4, max=35),
            user_exists_validator
        ]
    )
    password = PasswordField(
        'password',
        [validators.Required(), validators.Length(min=6, max=35)]
    )
