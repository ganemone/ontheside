from server.models.db import db


class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))