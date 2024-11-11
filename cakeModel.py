from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cake(Base):
    __tablename__ = 'cakes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    weight = Column(Float)

    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight
