#!/usr/bin/python3
"""
This script will list all of our state objects from database
hbtn_0e_6_usa
3 arguments:
- A MySQL username
- A MySQL password
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
    Session = sessionmaker(bind=engine)
    session = Session()

    for states in session.query(State).order_by(State.id).all():
        print("{}: {}".format(states.id, states.name))

    session.close()
