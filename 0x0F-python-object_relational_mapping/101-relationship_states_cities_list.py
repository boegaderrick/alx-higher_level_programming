#!/usr/bin/python3
"""
    This script queries a database for states and prints the returned
    values in ascending order of their ids
    Their relations (i.e cities) are printed below them respectively
"""
if __name__ == '__main__':
    from relationship_city import City
    from relationship_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    string = f'mysql+mysqldb://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(string)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(str(state.id) + ': ' + str(state.name))
        for city in state.cities:
            print('\t' + str(city.id) + ': ' + str(city.name))
