from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/flask'
db = SQLAlchemy(app)

class login11(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    dob = db.Column(db.Date, nullable=True)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/authenticate", methods=["POST"])
def authenticate():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = login11.query.filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.id
            flash("Login successful!", "success")
            return redirect(url_for('welcome'))
        else:
            flash("Invalid email or password", "error")
            return render_template("login.html")

@app.route("/welcome")
def welcome():
    if 'user_id' in session:
        user_id = session['user_id']
        user = login11.query.get(user_id)
        return render_template("welcome.html", user=user)
    else:
        return redirect(url_for('login'))

@app.route("/register", methods=["GET", "POST"])
def registering():
    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        password = request.form.get("password")
        dob = request.form.get("dob")

        dob = datetime.strptime(dob, "%Y-%m-%d").date() if dob else None

        new_user = login11(firstname=firstname, lastname=lastname, email=email, password=password, dob=dob)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.", "success")

        return redirect(url_for('login'))
    else:
        return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True, port=7081)
