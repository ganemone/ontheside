from server.models.db import db


class ProjectFavorite(db.Model):
    __tablename__ = 'project_favorites'
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
    project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'), primary_key=True)

    project = db.relationship('Project', backref=db.backref('project_favorite'))

    user = db.relationship('User', backref=db.backref('project_favorite'))

    def __init__(self, project=None, user=None):
        self.project = project
        self.user = user