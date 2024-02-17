#!/usr/bin/python3
""" Define a class City """

import sqlalchemy
from sqlalchemy import *
from model_state import Base, State


class City(Base):
    """ City representation """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

