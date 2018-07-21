#!/usr/bin/python3
"""
This script will print the state object with name as argument
from our hbtn_0e_6_usa database
4 arguments:
- A mysql username
- A mysql password
- A database name
- A state name to search
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).all()

    if len(state) == 0:
        print("Not found")

    else:
        for name in state:
            print("{}".format(name.id))

    session.close()
