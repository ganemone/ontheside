import json

from server.tests.helpers import FlaskTestCase, fixtures


class TestProjectAPI(FlaskTestCase):
    @fixtures('base.json')
    def test_get_empty_projects(self):
        """Test GET /api/projects endpoint with no data"""
        response, data = self.api_request('get', '/api/projects')
        assert data['num_results'] is 0
        assert response.status_code == 200

    @fixtures('single_project.json')
    def test_get_one_project(self):
        """Test GET /api/projects endpoint with a single project"""
        response, data = self.api_request('get', '/api/projects')
        assert data['num_results'] is 1
        assert response.status_code == 200

    @fixtures('many_projects.json')
    def test_get_multiple_projects(self):
        """Test GET /api/projects endpoint with multple projects"""
        response, data = self.api_request('get', '/api/projects')
        assert data['num_results'] > 0
        assert response.status_code == 200

    @fixtures('many_projects.json')
    def test_get_no_project_by_id(self):
        """Test GET /api/projects/(int:id) for missing project"""
        response, data = self.api_request('get', '/api/projects/1000')
        assert response.status_code == 404

    @fixtures('many_projects.json')
    def test_project_by_id(self):
        """Test GET /api/projects(int:id) for existing project"""
        response, data = self.api_request('get', '/api/projects/1')
        assert data['name'] == 'Some Project Name'
        assert 'users' in data
        assert 'keywords' in data
        assert 'languages' in data
        assert response.status_code == 200

    @fixtures('base.json')
    def test_post_project_unauthorized(self):
        data = {
            'name': 'Some Project',
            'description': 'Some Description',
            'source': 'somesource',
            'type': 'git'
        }
        response = self.app.post(
            '/api/projects',
            data=json.dumps(data)
        )

        assert response.status_code == 401

    @fixtures('many_projects.json')
    def test_post_project(self):
        self.login()

        data = {
            'name': 'Some Project',
            'description': 'Some Description',
            'source': 'somesource',
            'type': 'git',
            'keywords':
                [
                    {
                        'id': 1
                    }
                ],
            'languages':
                [
                    {
                        'id': 1
                    }
                ]
        }
        response = self.app.post(
            '/api/projects',
            data=json.dumps(data)
        )

        assert response.status_code == 201

