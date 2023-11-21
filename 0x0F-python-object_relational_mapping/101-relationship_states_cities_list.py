#!/usr/bin/python3
"""script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
"""

from os import listdir
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# metadata = MetaData()


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    conn = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    list = session.query(State).order_by(State.id).all()

    for state in list:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t", end="")
            print("{}: {}".format(city.id, city.name))
    session.close()
    conn.close()
