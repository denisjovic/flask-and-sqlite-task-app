from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

db = SQL("sqlite:///users.db")

@app.route("/")
def index():
	# Select all data from the users database
	rows = db.execute("SELECT * FROM users")
	return render_template("index.html", rows=rows )

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	else:
		# Extract name and email from post request
		name = request.form.get("name")
		if not name:
			return render_template("404.html", message="You must enter name!")
		email = request.form.get("email")
		if not email:
			return render_template("404.html", message="You must enter email!")
		# Insert name, email to the database
		db.execute("INSERT into users (name, email) VALUES (:name, :email)", name=name, email=email);
		# Redirect user back to home page
		return redirect("/")

