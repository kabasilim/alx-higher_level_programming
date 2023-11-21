#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""

from importlib.metadata import metadata
import sys
from model_state import Base, State

from sqlalchemy import create_engine, MetaData, select

metadata = MetaData()


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    conn = engine.connect()
    r = conn.execute('SELECT * FROM states ORDER BY states.id ASC')
    data = r.fetchone()

    if data:
        print("{}: {}".format(data[0], data[1]))
    else:
        print("Nothing")

    conn.close()
