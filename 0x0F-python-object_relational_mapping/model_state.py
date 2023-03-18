#!/usr/bin/python3
"""This module define a class mapped to a db"""
import SQLAlchemy
import MySQLdb
import sys
from sqlalchemy import create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column

host = 'localhost'
port = 3306
user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

string = f'mysql+mysqldb://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(string)
Base = declarative_base()


class State(Base):
    """State class definition"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

Base.metadata.create_all(engine)
