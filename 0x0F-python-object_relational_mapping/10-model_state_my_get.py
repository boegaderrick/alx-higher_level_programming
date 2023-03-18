#!/usr/bin/python3
"""
    This script queries state id from a database and prints it
    If the state was not found it prints 'Not found'
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
    state_name = sys.argv[4]

    string = f'mysql+mysqldb://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(string)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_id = session.query(State.id).order_by(
                            State.id).filter(State.name == state_name).first()
    print(state_id[0] if state_id else 'Not found')
