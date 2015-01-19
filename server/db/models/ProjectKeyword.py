from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
Base = declarative_base()


class ProjectKeyword(Base):
    __tablename__ = 'project_keywords'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    keyword_id = Column(Integer, ForeignKey('keywords.id'))
