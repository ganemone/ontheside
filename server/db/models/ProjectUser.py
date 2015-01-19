from sqlalchemy import Column, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
Base = declarative_base()


class ProjectUser(Base):
    __tablename__ = 'project_users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))
    role = Column(Enum('owner', 'contributer', 'designer'))
