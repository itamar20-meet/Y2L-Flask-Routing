from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from model import Cart, Product
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

Id = Product1.Id

@app.route("/")
def home_page():
	return render_template("home.html")

@app.route("/store_page", methods=['GET', 'POST'])
def store_page():	
	if request.method == 'GET':
		return render_template("store.html",p=Product1.Picture_Link, n=Product1.name,pr=Product1.Price, d=Product1.Description)
	else:
		add_to_cart(annoyingError(),Id)
		selected_product=query_by_id(annoyingError(), Id)

		return render_template("cart.html",p=selected_product.Picture_Link, n=selected_product.name,pr=selected_product.Price, d=selected_product.Description)

@app.route("/about_page")
def about_page():
	return render_template("about.html")

@app.route("/login_page")
def login_page():
		return render_template("login.html")
			


if __name__ == '__main__':
	app.run(debug=True)