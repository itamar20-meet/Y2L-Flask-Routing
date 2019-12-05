from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from model import Cart, Product
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route("/")
def home_page():
	return render_template("home.html")

@app.route("/store_page", methods=['GET', 'POST'])
def store_page():	
	if request.method == 'GET':
		return render_template("store.html",p=Product1.Picture_Link, n=Product1.name,pr=Product1.Price, d=Product1.Description)
	else:
		add_to_cart(Product1.Id)
		selected_product=query_by_id(Product1.Id)
		return render_template("cart.html",p=selected_product.Picture_Link, n=selected_product.name,pr=selected_product.Price, d=selected_product.Description)

@app.route("/about_page")
def about_page():
	return render_template("about.html")
@app.route("/login_page", methods=['GET', 'POST'])
def login_page():
	if request.method == 'POST':
			render_template()	


if __name__ == '__main__':
    app.run(debug=True)