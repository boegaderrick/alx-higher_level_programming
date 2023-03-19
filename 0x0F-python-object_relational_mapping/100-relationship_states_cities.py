#!/usr/bin/python3
"""
    This script creates a State object and a City object related to it
    It also creates corresponding tables in a user specified database
    The objects are then mapped to their respective tables.
"""
if __name__ == '__main__':
    from relationship_city import City, State, Base
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
    Base.metadata.create_all(engine)

    california = State(name='California')
    san_f = City(name='San Francisco', state=california)

    session.add(california)
    session.add(san_f)
    session.commit()
