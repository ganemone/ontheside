from app_factory import db


# Project Users Table
id = db.Column('id', db.Integer, primary_key=True)
user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
role = db.Column('role', db.Enum('owner', 'contributer', 'designer'))
project_users = db.Table('project_users', id, user_id, project_id, role)

# Project Keywords Table
id = db.Column('id', db.Integer, primary_key=True)
keyword_id = db.Column('keyword_id', db.Integer, db.ForeignKey('keywords.id'))
project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
project_keywords = db.Table('project_keywords', id, keyword_id, project_id)

# Project Languages
id = db.Column('id', db.Integer, primary_key=True)
language_id = db.Column(
    'language_id', db.Integer, db.ForeignKey('languages.id'))
project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
project_languages = db.Table('project_languages', id, language_id, project_id)


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    source = db.Column(db.String(256))
    type = db.Column(db.Enum('bitbucket', 'git'))

    users = db.relationship('User', secondary=project_users)
    keywords = db.relationship('Keyword', secondary=project_keywords)
    languages = db.relationship('Language', secondary=project_languages)
