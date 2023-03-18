#!/usr/bin/python3
"""
    This adds a state record to a database
    The id value is printed after completion
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
    louisiana = State(name='Louisiana')
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
