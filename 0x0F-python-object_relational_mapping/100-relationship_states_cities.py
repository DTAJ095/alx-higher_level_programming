#!/usr/bin/python3
""" script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa
"""

import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = State(name='California')
    state_name.cities = [City(name='San Francisco')]
    session.add(state_name)
    session.commit()
    session.close()
