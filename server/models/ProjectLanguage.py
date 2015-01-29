from app_factory import db


class ProjectLanguage(db.Model):
    __tablename__ = 'project_languages'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
