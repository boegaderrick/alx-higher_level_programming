#!/usr/bin/python3
"""
    This script queries for cities, their id's and home states in database
    The result is printed in a custom format
"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == '__main__':
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    string = f'mysql+mysqldb://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(string)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State.name, City.id, City.name).filter(
                                City.state_id == State.id).order_by(City.id)
    for value in cities:
        print(f'{value[0]}: ({value[1]}) {value[2]}')
