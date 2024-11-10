from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cake(Base):
    __tablename__ = 'cakes'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    flavor = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"Cake(id={self.id}, name='{self.name}', flavor='{self.flavor}', price={self.price})"
