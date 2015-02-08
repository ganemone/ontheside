from sqlalchemy.ext.associationproxy import association_proxy

from server.models.db import db
from server.models.user import User


# Project Keywords Table
p_id = db.Column('id', db.Integer, primary_key=True)
keyword_id = db.Column('keyword_id', db.Integer, db.ForeignKey('keywords.id'))
project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
project_keywords = db.Table('project_keywords', p_id, keyword_id, project_id)

# Project Languages
pr_id = db.Column('id', db.Integer, primary_key=True)
language_id = db.Column(
    'language_id', db.Integer, db.ForeignKey('languages.id'))
project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
project_languages = db.Table(
    'project_languages', pr_id, language_id, project_id
)


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    source = db.Column(db.String(256))
    type = db.Column(db.Enum('bitbucket', 'git'))

    users = association_proxy('project_user', 'user')
    keywords = db.relationship('Keyword', secondary=project_keywords)
    languages = db.relationship('Language', secondary=project_languages)

    def _get_users_with_role(self, role: str) -> list:
        """Returns a list of users corresponding to the
            project with a role
    
            :param role: role of user | owner || contributer || designer
            :return: list of users corresponding to the given role
            """
        return list(filter(lambda x: x.role == role, self.users.col))

    @property
    def owners(self) -> list:
        """Returns a list of project owners

        :return: a list of usernames of project owners
        """
        return self._get_users_with_role('owner')

    @property
    def contributers(self) -> list:
        """Returns a list of project contributers

        :return: a list of project contributers
        """
        return self._get_users_with_role('contributer')

    @property
    def designers(self) -> list:
        """Returns a list of project designers

        :return: a list of project designers
        """
        return self._get_users_with_role('designer')


class ProjectUsers(db.Model):
    __tablename__ = 'project_users'
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
    project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    role = db.Column('role', db.Enum('owner', 'contributer', 'designer'))

    project = db.relationship(Project, backref=db.backref('project_user'))

    user = db.relationship(User, backref=db.backref('project_user'))

    def __init__(self, project=None, user=None, role=None):
        self.project = project
        self.user = user
        self.role = role
