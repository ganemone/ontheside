from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
Base = declarative_base()


class ProjectLanguage(Base):
    __tablename__ = 'project_languages'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    language_id = Column(Integer, ForeignKey('languages.id'))
