from wtforms import Form, StringField, PasswordField, validators


class RegistrationForm(Form):
    """Form for handling registration form validation
    """
    username = StringField(
        'username',
        [validators.required(),
         validators.Length(min=4, max=25)]
    )
    password = PasswordField(
        'password',
        [validators.required(),
         validators.Length(min=6, max=35),
         validators.EqualTo('confirm')]
    )
    confirm = PasswordField('confirm')
    email = StringField(
        'email',
        [validators.required(),
         validators.length(min=6, max=35)]
    )
