#!/usr/bin/python3
"""
This script will print all of the city objects from our database
hbtn_0e_14_usa
3 arguments:
- A mysql username
- A mysql password
- A database name
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for City, State in session.query(City, State).join(State).order_by(
            City.id):
        print("{}: ({}) {}".format(State.name, City.id, City.name))

    session.close()
