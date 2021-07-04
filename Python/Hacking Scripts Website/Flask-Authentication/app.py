from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import jinja2
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",  "sqlite:///users.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##Create table in data base
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# db.create_all only once
db.create_all()

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form
        if User.query.filter_by(email=data["email"]).first():
            flash("You are already registered,instead Login")
            return redirect(url_for("login"))
        # Using hashing and salting while creating password
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            email=data["email"],
            name=data["name"],
            password=hash_and_salted_password
        )

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets", name=new_user.name))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form
        email = data["email"]
        password = data["password"]
        user = User.query.filter_by(email=email).first()
        # Using flask flash messages for errors
        if not user:
            flash('Please register first')
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, password):
            flash("Incorrect Password")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("secrets", name=user.name))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets/<name>')
def secrets(name):
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
