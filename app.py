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
	if request.method == 'GET' :
		return render_template("store.html")
	else:
		Product=add_product("https://images-na.ssl-images-amazon.com/images/I/31%2BSnEw8mjL._SX425_.jpg","katana",199.99,"a f*cking katana")
		return render_template("store.html")
@app.route("/cart_page")
def cart_page():

	return render_template("cart.html")

@app.route("/about_page")
def about_page():
	return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)