from flask_login import UserMixin

from server.models.db import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(50))
    username = db.Column('username', db.String(50))
    password = db.Column('password', db.String(50))
    email = db.Column('email', db.String(128))

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
