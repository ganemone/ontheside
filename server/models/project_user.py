from server.models.db import db


class ProjectUser(db.Model):
    __tablename__ = 'project_users'
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
    project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    role = db.Column('role', db.Enum('owner', 'contributer', 'designer'))

    project = db.relationship('Project', backref=db.backref('project_user'))

    user = db.relationship('User', backref=db.backref('project_user'))

    def __init__(self, project=None, user=None, role=None):
        self.project = project
        self.user = user
        self.role = role