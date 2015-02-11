from sqlalchemy.ext.associationproxy import association_proxy

from server.models.db import db
from server.models.user import User


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    source = db.Column(db.String(256))
    type = db.Column(db.Enum('bitbucket', 'git'))

    users = association_proxy('project_user', 'user')
    languages = db.relationship('Language', secondary='project_languages')
    keywords = db.relationship('Keyword', secondary='project_keywords')

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
