#!/usr/bin/python3
"""
This script will delete all the state objects with a name containing
the letter a from our database hbtn_0e_6_usa
3 arguments:
- A msyql username
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
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.contains("a")
                                ).delete(synchronize_session=False)

    session.commit()
    session.close()
