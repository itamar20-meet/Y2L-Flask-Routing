from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_product( Picture_Link,name, price, Description):
    product_object = Product(
        Picture_Link=Picture_Link,
        name=name,
        price=price,
        Description=Description)
    session.add(product_object)
    session.commit()

def delete_product(their_id):
   session.query(Product).filter_by(
       id=their_id).delete()
   session.commit()

def choose(x):
  if x==1:
    Picture_Link="https://amp.businessinsider.com/images/5849956cba6eb61b008b8256-750-562.jpg"
    name="pot"
    price=19.99
    description="The good stuff"
  elif x==2:
    Picture_Link=""
    name="Eminem"
    price=9.99
    description="For munchies"
  elif x==3:
    Picture_Link=""
    name="Katana"
    price=199.99
    description="For after munchies"
  else:
    Picture_Link="https://amp.businessinsider.com/images/5849956cba6eb61b008b8256-750-562.jpg"
    name="pot"
    price=19.99
    description="The good stuff"


def query_all():
   products = session.query(
      Product).all()
   return products

def query_by_id(their_id):
   products = session.query(
       Student).filter_by(
       id=their_id)
   return products

def add_to_cart(product_id):
    cart_object = Product(
        product_id=product_id)
    session.add(cart_object)
    session.commit()

