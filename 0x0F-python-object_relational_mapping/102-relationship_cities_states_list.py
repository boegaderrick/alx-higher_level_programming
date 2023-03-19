#!/usr/bin/python3
"""
    This script queries for city records in a database
    The resulting city ids and names are then printed alongside related states
"""
if __name__ == '__main__':
    from relationship_city import City
    from relationship_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    string = f'mysql+mysqldb://{user}:{password}@localhost:3306/{database}'
    session = sessionmaker(bind=create_engine(string))()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')
