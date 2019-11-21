from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
   __tablename__ = 'Product'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   Price = Column(Float)
   Picture_Link = Column(String)
   Description = Column(String)

class Cart(Base):
   __tablename__ = 'Cart'
   id = Column(Integer, primary_key=True)
   product_id = Column(String)