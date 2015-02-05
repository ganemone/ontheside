from server.mod_auth.auth import load_user  # , register, login
from server.tests.helpers import FlaskTestCase, fixtures


class TestAuth(FlaskTestCase):
    @fixtures('single_user.json')
    def test_load_existing_user(self):
        """Test loading a single valid user"""
        with self.flaskapp.test_request_context():
            user = load_user(1)
            assert user is not None
            assert user.username == 'ganemone'

    @fixtures('base.json')
    def test_load_nonexisting_user(self):
        """Test loading a user not in the database"""
        with self.flaskapp.test_request_context():
            user = load_user(50)
            assert user is None
