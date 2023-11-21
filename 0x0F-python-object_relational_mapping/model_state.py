#!/usr/bin/python3
"""The state class model"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """The State class which inherits from the base"""

    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
