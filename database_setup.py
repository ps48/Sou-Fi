import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Msgkey(Base):
    __tablename__ = 'msgkey'

    hash_key = Column(String(6), primary_key=True)
    name = Column(String(250), nullable=False)


engine = create_engine('sqlite:///soufi.db')


Base.metadata.create_all(engine)
