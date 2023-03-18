#!/usr/bin/python3
"""
    This script modifies a record name
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
    state = session.query(State).filter(State.id == 2).one()
    state.name = 'New Mexico'
    session.commit()
