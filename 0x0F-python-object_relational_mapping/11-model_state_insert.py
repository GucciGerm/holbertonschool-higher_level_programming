#!/usr/bin/python3
"""
This script will add state object Louisiana to our hbtn_0e_6_usa
database
3 arguments:
- A mysql username
- A mysql password
- A database name
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
    Louie = State(name="Louisiana")
    session.add(Louie)
    session.commit()
    print(Louie.id)
    session.close()
