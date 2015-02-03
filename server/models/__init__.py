from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin

db = SQLAlchemy()


class Keyword(db.Model):
    __tablename__ = 'keywords'
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(128))


class Language(db.Model):
    __tablename__ = 'languages'
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(128))


# Project Users Table
u_id = db.Column('id', db.Integer, primary_key=True)
user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
role = db.Column('role', db.Enum('owner', 'contributer', 'designer'))
project_users = db.Table('project_users', u_id, user_id, project_id, role)

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
    description = db.Column(db.Text)
    source = db.Column(db.String(256))
    type = db.Column(db.Enum('bitbucket', 'git'))

    users = db.relationship('User', secondary=project_users)
    keywords = db.relationship('Keyword', secondary=project_keywords)
    languages = db.relationship('Language', secondary=project_languages)


class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(50))
    username = db.Column('username', db.String(50))
    password = db.Column('password', db.String(50))
    email = db.Column('email', db.String(128))

    session = db.relationship(
        Session, uselist=False, backref=db.backref('user', order_by=id)
    )

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
