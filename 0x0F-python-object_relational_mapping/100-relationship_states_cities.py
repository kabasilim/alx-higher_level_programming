#!/usr/bin/python3
"""script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
"""

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

    newState = State(name='California')
    newCity = City(name='San Francisco')

    newState.cities.append(newCity)
    session.add(newState)
    session.add(newCity)
    session.commit()
    session.close()
    conn.close()
