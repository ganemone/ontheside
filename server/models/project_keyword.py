from server.models.db import db


class ProjectKeyword(db.Model):
    __tablename__ = 'project_keywords'
    keyword_id = db.Column('keyword_id', db.Integer, db.ForeignKey('keywords.id'), primary_key=True)
    project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'), primary_key=True)

    project = db.relationship('Project', backref=db.backref('project_keyword'))

    keyword = db.relationship('Keyword', backref=db.backref('project_keyword'))

    def __init__(self, project=None, keyword=None, role=None):
        self.project = project
        self.keyword = keyword
        self.role = role