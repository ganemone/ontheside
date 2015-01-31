from app_factory import db
from models.session import Session


class User(db.Model):
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
        return ''
        '<User(name={name}, username={username}, '
        'password={password}, email={email})>'.format(
            name=self.name, username=self.username,
            password=self.password, email=self.email
        )

    def is_authenticated(self):
        return (hasattr(self.session.session_id) and
                self.session.session_id is not None)

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
