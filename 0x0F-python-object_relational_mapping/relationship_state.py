#!/usr/bin/python3
"""The state class model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

# Base = declarative_base()


class State(Base):
    """The State class which inherits from the base"""

    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
