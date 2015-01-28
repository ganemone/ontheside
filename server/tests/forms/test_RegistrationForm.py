import wtforms_json
import pytest

from forms.RegistrationForm import RegistrationForm

wtforms_json.init()


class TestRegistrationForm:

    def test_valid(self):
        json = {
            'username': 'someusername',
            'password': 'password',
            'confirm': 'confirm',
            'email': 'someemail@email.com'
        }

        form = RegistrationForm.from_json(json)
        assert (form.validate())
