from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
Base = declarative_base()


class Session(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    session_id = Column(String(128))
    user_id = Column(Integer, ForeignKey('users.id'))
