#!/usr/bin/python3
"""
This script will print the very first state object from database
hbtn_0e_6_usa
3 arguments:
- A mysql username
- A mysql password
- A database name
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
