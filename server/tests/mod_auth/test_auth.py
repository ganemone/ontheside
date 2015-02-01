import json
from mod_auth.auth import load_user  # , register, login
from tests.helpers import FlaskTestCase, fixtures


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


class TestPostUser(FlaskTestCase):

    @fixtures('keywords.json')
    def test_get_users(self):

        response = self.test_client.get('/api/keywords')
        assert response.status_code is 200

    @fixtures('base.json')
    def test_post_user(self):
        data = {
            'name': 'Giancarlo Anemone',
            'username': 'ganemone',
            'email': 'ganemone@gmail.com',
            'password': 'password',
            'confirm': 'password'
        }
        response = self.app.post(
            '/api/users',
            data=json.dumps(data)
        )

        assert response.status_code is 201
