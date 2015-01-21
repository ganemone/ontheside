from app_factory import db
from db.models.Session import Session


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

    def __repr__(self):
        return ''
        '<User(name={name}, username={username}, '
        'password={password}, email={email})>'.format(
            name=self.name, username=self.username,
            password=self.password, email=self.email
        )
