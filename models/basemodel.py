#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, DATETIME
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
'''
Initialize database connection and create the base class for all models.
'''

# Database configuration
user = 'simplepos_usr'
password = 'simplepos_pwd'
host = 'localhost'
port = '3306'
db = 'simplepos'

# Create base class
Base = declarative_base()

# Create engine
engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}:{port}/{db}')

# Create session
Session = sessionmaker(bind=engine)
session = Session()


class BaseModel(Base):
    '''
    Base class for all models.
    '''
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DATETIME, default=datetime.utcnow, nullable=False)
    updated_at = Column(DATETIME,
                        default=datetime.utcnow,
                        onupdate=datetime.utcnow,
                        nullable=False)

    def create(self):
        '''
        Create a new record.
        '''
        session.add(self)
        session.commit()
        return self

    def get(self, id):
        '''
        Get a record by id.
        '''
        return session.query(self.__class__).get(id)

    def save(self):
        '''
        Update a record.
        '''
        session.commit()
        return self

    def delete(self):
        '''
        Delete a record.
        '''
        session.delete(self)
        session.commit()


# Create all database tables
Base.metadata.create_all(engine)
