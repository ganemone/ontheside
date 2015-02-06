from flask_login import UserMixin
from sqlalchemy.ext.associationproxy import association_proxy
from server.models.db import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(50))
    username = db.Column('username', db.String(50))
    password = db.Column('password', db.String(50))
    email = db.Column('email', db.String(128))

    projects = association_proxy('project_user', 'project')

    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        ret = ''
        '<User(name={name}, username={username}, '
        'password={password}, email={email})>'.format(
            name=self.name, username=self.username,
            password=self.password, email=self.email
        )
        return ret

    def _get_projects_with_role(self, role: str) -> list:
        """Gets list of projects corresponding to a given role

        :param role: role to filter projects against (owner | contributer | designer)
        :return: list of projects filtered against the role
        """
        return list(filter(lambda x: x.role == role, self.projects.col))

    @property
    def owned_projects(self) -> list:
        """Gets projects owned by user
        :return: list of projects owned by user
        """
        return self._get_projects_with_role('owner')

    @property
    def designer_projects(self) -> list:
        """Returns list of projects user is designer on
        :return: list of designer projects
        """
        return self._get_projects_with_role('designer')

    @property
    def contributer_projects(self) -> list:
        """Returns list of projects user is contributer on
        :return: list of contributer projects
        """
        return self._get_projects_with_role('contributer')

