from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route("/")
def home_page():
	return render_template("home.html")

@app.route("/store_page")
def store_page():
	return render_template("store.html")
def choose(x):
	if x==1:
		Picture_Link="https://amp.businessinsider.com/images/5849956cba6eb61b008b8256-750-562.jpg"
		price=19.99
		name="pot"
		descroption="The good stuff"
	elif x==2:
		Picture_Link=""
		price=9.99
		name="Eminem"
		descroption="For munchies"
	elif x==3:
		Picture_Link=""
		price=199.99
		name="Katana"
		descroption="For after munchies"
	else:
		pass

@app.route("/cart_page")
def cart_page():
	return render_template("cart.html")

@app.route("/about_page")
def about_page():
	return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)