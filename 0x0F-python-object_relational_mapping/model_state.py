#!/usr/bin/python3
""" python file that contains the class definition of a State
    and an instance Base = declarative_base()
"""

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State representation """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
