#!/usr/bin/python3
"""script that lists all City objects from
the database hbtn_0e_101_usa
"""

import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
