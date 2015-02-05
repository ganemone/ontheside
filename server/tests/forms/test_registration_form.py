from server.tests.helpers import SimpleTestCase
from server.forms import RegistrationForm


class TestRegistrationForm(SimpleTestCase):
    def test_valid(self):
        json = {
            'username': 'someusername',
            'password': 'password',
            'confirm': 'password',
            'email': 'someemail@email.com'
        }

        form = RegistrationForm.from_json(json)
        assert (form.validate())

    def test_missing_username(self):
        json = {
            'password': 'password',
            'confirm': 'password',
            'email': 'someemail@email.com'
        }
        form = RegistrationForm.from_json(json)
        assert form.validate() is False

    def test_missing_password(self):
        json = {
            'username': 'someusername',
            'confirm': 'password',
            'email': 'someemail@email.com'
        }
        form = RegistrationForm.from_json(json)
        assert form.validate() is False

    def test_missing_confirm(self):
        json = {
            'username': 'someusername',
            'password': 'password',
            'email': 'someemail@email.com'
        }
        form = RegistrationForm.from_json(json)
        assert form.validate() is False

    def test_missing_email(self):
        json = {
            'username': 'someusername',
            'password': 'password',
            'confirm': 'password',
        }
        form = RegistrationForm.from_json(json)
        assert form.validate() is False

    def test_invalid_password_combination(self):
        json = {
            'username': 'someusername',
            'password': 'password',
            'confirm': 'WRONG',
            'email': 'someemail@email.com'
        }
        form = RegistrationForm.from_json(json)
        assert form.validate() is False
