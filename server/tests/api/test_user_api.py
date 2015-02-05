import json

from server.tests.helpers import FlaskTestCase, fixtures


class TestUserAPI(FlaskTestCase):
    @fixtures('base.json')
    def test_get_empty_users(self):
        """Test GET /api/users endpoint with no data"""
        response, data = self.api_request('get', '/api/users')
        assert data['num_results'] is 0
        assert response.status_code is 200

    @fixtures('single_user.json')
    def test_get_one_user(self):
        """Test GET /api/users endpoint with a single user"""
        response, data = self.api_request('get', '/api/users')
        assert data['num_results'] is 1
        assert response.status_code is 200

    @fixtures('many_users.json')
    def test_get_multiple_users(self):
        """Test GET /api/users endpoint with multple users"""
        response, data = self.api_request('get', '/api/users')
        assert data['num_results'] > 0
        assert response.status_code is 200

    @fixtures('many_users.json')
    def test_get_no_user_by_id(self):
        """Test GET /api/users/(int:id) for missing user"""
        response, data = self.api_request('get', '/api/users/1000')
        assert response.status_code == 404

    @fixtures('many_users.json')
    def test_user_by_id(self):
        """Test GET /api/users(int:id) for existing user"""
        response, data = self.api_request('get', '/api/users/1')
        assert data['username'] == 'ganemone'
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
