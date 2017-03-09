#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    __tablename__ = "states"