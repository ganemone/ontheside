from sqlalchemy import create_engine, Column, Integer, String, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
Base = declarative_base()

engine = create_engine('mysql+pymysql://root:root@localhost/ontheside')

Session = sessionmaker(bind=engine)
session = Session()


session.add(ed_user)
session.commit()
