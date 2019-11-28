from model import Base, Product, Cart 


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_product( Picture_Link,name, Price, Description):
    product_object = Product(
        Picture_Link=Picture_Link,
        name=name,
        Price=Price,
        Description=Description)
    session.add(product_object)
    session.commit()

def delete_product(their_id):
   session.query(Product).filter_by(
       id=their_id).delete()
   session.commit()



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



