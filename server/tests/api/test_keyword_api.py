import json

from server.tests.helpers import FlaskTestCase, fixtures


class TestKeywordAPI(FlaskTestCase):
    @fixtures('base.json')
    def test_get_empty_keywords(self):
        """Test GET /api/keywords endpoint with no data"""
        response, data = self.api_request('get', '/api/keywords')
        assert data['num_results'] is 0
        assert response.status_code == 200

    @fixtures('single_keyword.json')
    def test_get_one_keyword(self):
        """Test GET /api/keywords endpoint with a single keyword"""
        response, data = self.api_request('get', '/api/keywords')
        assert data['num_results'] is 1
        assert response.status_code == 200

    @fixtures('many_keywords.json')
    def test_get_multiple_keywords(self):
        """Test GET /api/keywords endpoint with multple keywords"""
        response, data = self.api_request('get', '/api/keywords')
        assert data['num_results'] > 0
        assert response.status_code == 200

    @fixtures('many_keywords.json')
    def test_get_no_keyword_by_id(self):
        """Test GET /api/keywords/(int:id) for missing keyword"""
        response, data = self.api_request('get', '/api/keywords/1000')
        assert response.status_code == 404

    @fixtures('many_keywords.json')
    def test_keyword_by_id(self):
        """Test GET /api/keywords(int:id) for existing keyword"""
        response, data = self.api_request('get', '/api/keywords/1')
        assert data['keyword'] == 'Web Development'
        assert response.status_code == 200

    @fixtures('single_user.json')
    def test_post_keyword(self):
        """Tests POST to /api/keywords for an authorized user"""
        self.login()

        data = {
            'keyword': 'some_value'
        }
        response = self.app.post(
            '/api/keywords',
            data=json.dumps(data)
        )

        assert response.status_code == 201

    @fixtures('base.json')
    def test_post_keyword_unauthorized(self):
        """Tests POST to /api/keywords for an unauthorized user"""
        data = {
            'keyword': 'some_value'
        }
        response = self.app.post(
            '/api/keywords',
            data=json.dumps(data)
        )

        assert response.status_code == 401
