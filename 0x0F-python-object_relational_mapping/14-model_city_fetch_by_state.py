#!/usr/bin/python3
"""script that lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa
"""

from importlib.metadata import metadata
import sys
from model_state import Base, State
from model_city import Base, City

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


metadata = MetaData()


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    conn = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    list = session.query(State.name, City.id, City.name)\
        .filter(City.state_id == State.id).order_by(City.id).all()

    for item in list:
        print("{}: ({}) {}".format(item[0], item[1], item[2]))

    session.close()
    conn.close()
