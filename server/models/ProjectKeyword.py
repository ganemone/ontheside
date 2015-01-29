from app_factory import db


class ProjectKeyword(db.Model):
    __tablename__ = 'project_keywords'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    keyword_id = db.Column(db.Integer, db.ForeignKey('keywords.id'))
