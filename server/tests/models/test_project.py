from server.models import Project
from server.tests.helpers import fixtures, FlaskTestCase


class TestProject(FlaskTestCase):

    @fixtures('single_project.json')
    def test_single_owner(self):
        """Test getting single project owner
        """
        with self.flaskapp.test_request_context():
            project = Project.query.filter_by(id=1).first()
            owners = project.owners
            assert len(owners) is 1

    @fixtures('many_owners.json')
    def test_many_owners(self):
        """Test getting multiple project owners
        """
        with self.flaskapp.test_request_context():
            project = Project.query.filter_by(id=1).first()
            owners = project.owners
            assert len(owners) is 3

    @fixtures('single_contributer.json')
    def test_single_contributer(self):
        """Test getting single contributer
        """
        with self.flaskapp.test_request_context():
            project = Project.query.filter_by(id=1).first()
            contributers = project.contributers
            assert len(contributers) is 1

    @fixtures('many_contributers.json')
    def test_many_contributers(self):
        """Test getting many contributers
        """
        with self.flaskapp.test_request_context():
            project = Project.query.filter_by(id=1).first()
            contributers = project.contributers
            assert len(contributers) is 3

    @fixtures('single_designer.json')
    def test_single_designer(self):
        """Test getting single designer
        """
        with self.flaskapp.test_request_context():
            project = Project.query.filter_by(id=1).first()
            designers = project.designers
            assert len(designers) is 1

    @fixtures('many_designers.json')
    def test_many_designers(self):
        """Test getting many designers
        """
        with self.flaskapp.test_request_context():
            project = Project.query.filter_by(id=1).first()
            designers = project.designers
            assert len(designers) is 2