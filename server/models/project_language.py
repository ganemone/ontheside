from server.models.db import db


class ProjectLanguage(db.Model):
    __tablename__ = 'project_languages'
    language_id = db.Column('language_id', db.Integer, db.ForeignKey('languages.id'), primary_key=True)
    project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'), primary_key=True)

    project = db.relationship('Project', backref=db.backref('project_language'))

    language = db.relationship('Language', backref=db.backref('project_language'))

    def __init__(self, project=None, language=None, role=None):
        self.project = project
        self.language = language
        self.role = role