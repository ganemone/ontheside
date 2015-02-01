import json
from tests.helpers import FlaskTestCase, fixtures


class TestUserAPI(FlaskTestCase):

    @fixtures('base.json')
    def test_get_empty_users(self):
        """Test GET /api/users endpoint with no data"""
        response = self.test_client.get('/api/users')
        assert response.status_code is 200

    def test_get_one_user(self):
        """Test GET /api/users endpoint with a single user"""

    def test_get_multiple_users(self):
        """Test GET /api/users endpoint with multple users"""

    def test_get_no_user_by_id(self):
        """Test GET /api/users/(int:id) for missing user"""

    def test_user_by_id(self):
        """Test GET /api/users(int:id) for existing user"""

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
