from wtforms import Form, StringField, PasswordField, validators


class RegistrationForm(Form):
    username = StringField(
        [validators.Required(), validators.Length(min=4, max=25)]
    )
    password = PasswordField(
        [validators.Required(),
         validators.Length(min=6, max=35),
         validators.EqualTo('confirm')]
    )
    confirm = PasswordField()
    email = StringField([
        validators.Required(),
        validators.length(min=6, max=35)]
    )
