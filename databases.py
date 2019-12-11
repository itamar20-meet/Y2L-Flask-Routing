from model import Base, Product, Cart 


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def annoyingError():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session


def add_product(session, Picture_Link,name, Price, Description):
		product_object = Product(
				Picture_Link=Picture_Link,
				name=name,
				Price=Price,
				Description=Description)
		session.add(product_object)
		session.commit()
		return product_object

def delete_product(session,their_id):
	 session.query(Product).filter_by(
			 id=their_id).delete()
	 session.commit()



def query_all(session):
	 products = session.query(
			Product).all()
	 return products

def query_by_id(session, Id):
	 product = session.query(
			 Product).filter_by(
			 Id=Id).first()
	 return product

def add_to_cart(session, product_id):
		cart_object = Cart(
			product_id=product_id)
		session.add(cart_object)
		session.commit()



Product1=add_product(annoyingError(), "https://images-na.ssl-images-amazon.com/images/I/31%2BSnEw8mjL._SX425_.jpg","katana",199.99,"a f*cking katana")
