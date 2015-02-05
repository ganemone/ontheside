from server.tests.helpers import FlaskTestCase, fixtures
from server.forms import LoginForm

invalid_combo_message = 'Invalid username/password combination'


class TestLoginForm(FlaskTestCase):
    @fixtures('many_users.json')
    def test_nonexisting_user(self):
        """Test login form validation with nonexisting user"""
        with self.flaskapp.test_request_context():
            form = LoginForm.from_json({
                'username': 'nonexisting',
                'password': 'password'
            })
            assert form.validate() is False
            assert len(form.errors['username']) is 1
            assert form.errors['username'][0] == invalid_combo_message

    @fixtures('many_users.json')
    def test_invalid_password(self):
        """Test login form validation with invalid username/password
        combination"""
        with self.flaskapp.test_request_context():
            form = LoginForm.from_json({
                'username': 'ganemone',
                'password': 'invalid'
            })
            assert form.validate() is False
            assert len(form.errors['username']) is 1
            assert form.errors['username'][0] == invalid_combo_message

    def test_invalid_empty_form(self):
        """Test login form validation with an empty form"""
        with self.flaskapp.test_request_context():
            form = LoginForm.from_json({})
            assert form.validate() is False

    def test_invalid_missing_username(self):
        """Test login form validation with a form missing the username"""
        with self.flaskapp.test_request_context():
            form = LoginForm.from_json({
                'password': 'password'
            })
            assert form.validate() is False

    def test_invalid_missing_password(self):
        """Test login form validation with a form missing the password"""
        with self.flaskapp.test_request_context():
            form = LoginForm.from_json({
                'username': 'ganemone'
            })
            assert form.validate() is False

    @fixtures('many_users.json')
    def test_valid_login_form(self):
        """Test login form validation with valid user"""
        with self.flaskapp.test_request_context():
            form = LoginForm.from_json({
                'username': 'ganemone',
                'password': 'password'
            })
            assert form.validate() is True
