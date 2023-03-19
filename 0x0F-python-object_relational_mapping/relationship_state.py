#!/usr/bin/python3
"""This module defines a class mapped to a database"""
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class definition"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')
