from sqlalchemy import Column, Integer, String, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    source = Column(String(256))
    type = Column(Enum('bitbucket', 'git'))

    users = relationship('User', secondary='project_users')
    keywords = relationship('Keyword', secondary='project_keywords')
    languages = relationship('Language', secondary='project_languages')
