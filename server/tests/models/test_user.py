from server.models import User
from server.tests.helpers import fixtures, FlaskTestCase


class TestUser(FlaskTestCase):

    @fixtures('many_projects.json')
    def test_no_projects(self):
        """Test getting projects on user with no projects
        """
        with self.flaskapp.test_request_context():
            user = User.query.filter_by(id=3).first()
            projects = user.owned_projects
            assert len(projects) is 0

    @fixtures('single_project.json')
    def test_single_owned_project(self):
        """Test getting single owned project
        """
        with self.flaskapp.test_request_context():
            user = User.query.filter_by(id=1).first()
            projects = user.owned_projects
            assert len(projects) is 1

    @fixtures('many_projects.json')
    def test_many_owned_projects(self):
        """Test getting many owned projects
        """
        with self.flaskapp.test_request_context():
            user = User.query.filter_by(id=2).first()
            projects = user.owned_projects
            assert len(projects) is 2

    @fixtures('many_projects.json')
    def test_contributer_project(self):
        """Test getting single contributer project
        """
        with self.flaskapp.test_request_context():
            user = User.query.filter_by(id=3).first()
            projects = user.contributer_projects
            assert len(projects) is 1

    @fixtures('many_projects.json')
    def test_designer_project(self):
        """Test getting many designers role projects
        """
        with self.flaskapp.test_request_context():
            user = User.query.filter_by(id=2).first()
            projects = user.designer_projects
            assert len(projects) is 1

