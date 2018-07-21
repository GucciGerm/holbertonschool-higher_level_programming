#!/usr/bin/python3
"""
A python script that contains the class definition of a state
and an instance of Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State - inherits from the base, links to the MySQL table states
    id - represents a column of an autogenerated, unique integer (Not null)
    name - represents a string with the max chars of 128 (Not null)
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)