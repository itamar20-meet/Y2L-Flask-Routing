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
def catalog(x):
	if x==1:
		pass
	elif x==2:
		pass
	elif x==3:
		pass
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