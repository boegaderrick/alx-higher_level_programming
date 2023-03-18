#!/usr/bin/python3
"""
    This script queries state name and id from a database
    It also applies a filter and orders by id value
    The results are printed in a custom format
"""
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
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
    states = session.query(State.id, State.name).order_by(
                            State.id).filter(State.name.ilike('%a%'))
    for state in states:
        print(str(state[0]) + ': ' + str(state[1]))
