from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(50))
    username = Column('username', String(50))
    password = Column('password', String(50))
    email = Column('email', String(128))

    session = relationship(
        'Session', uselist=False, backref=backref('user', order_by=id)
    )

    def __repr__(self):
        return ''
        '<User(name={name}, username={username}, '
        'password={password}, email={email})>'.format(
            name=self.name, username=self.username,
            password=self.password, email=self.email
        )
