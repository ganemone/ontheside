import json

from server.tests.helpers import FlaskTestCase, fixtures


class TestLanguageAPI(FlaskTestCase):
    @fixtures('base.json')
    def test_get_empty_languages(self):
        """Test GET /api/languages endpoint with no data"""
        response, data = self.api_request('get', '/api/languages')
        assert data['num_results'] is 0
        assert response.status_code == 200

    @fixtures('single_language.json')
    def test_get_one_language(self):
        """Test GET /api/languages endpoint with a single language"""
        response, data = self.api_request('get', '/api/languages')
        assert data['num_results'] is 1
        assert response.status_code == 200

    @fixtures('many_languages.json')
    def test_get_multiple_languages(self):
        """Test GET /api/languages endpoint with multple languages"""
        response, data = self.api_request('get', '/api/languages')
        assert data['num_results'] > 0
        assert response.status_code == 200

    @fixtures('many_languages.json')
    def test_get_no_language_by_id(self):
        """Test GET /api/languages/(int:id) for missing language"""
        response, data = self.api_request('get', '/api/languages/1000')
        assert response.status_code == 404

    @fixtures('many_languages.json')
    def test_language_by_id(self):
        """Test GET /api/languages(int:id) for existing language"""
        response, data = self.api_request('get', '/api/languages/1')
        assert data['language'] == 'Python'
        assert response.status_code == 200

    @fixtures('single_user.json')
    def test_post_language(self):
        """Tests POST to /api/languages for an authorized user"""
        self.login()

        data = {
            'language': 'some_value'
        }
        response = self.app.post(
            '/api/languages',
            data=json.dumps(data)
        )

        assert response.status_code == 201

    @fixtures('base.json')
    def test_post_language_unauthorized(self):
        """Tests POST to /api/languages for an unauthorized user"""
        data = {
            'language': 'some_value'
        }
        response = self.app.post(
            '/api/languages',
            data=json.dumps(data)
        )

        assert response.status_code == 401
