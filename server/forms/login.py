from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
    # Login name can be either username or email
    login_name = StringField(
        [validators.Required(), validators.Length(min=4, max=35)]
    )
    password = PasswordField(
        [validators.Required(), validators.Length(min=6, max=35)]
    )
