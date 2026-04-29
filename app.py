# Project Name: [Global Grub]
# License: MIT
# Copyright (c) 2026 [Colm Nolan]


from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from helpers import get_meal_by_id, search_meals, get_meals_by_region, get_countries
import os

# load local environment variables from .env
load_dotenv()

# initialize Flask app
app = Flask(__name__)

# app configuration
# require SECRET_KEY from environment/.env
app.secret_key = os.environ["SECRET_KEY"]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///globalgrub.db'

# initialize database and password hashing
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# setup login system
login_manager = LoginManager()
login_manager.init_app(app)

# redirect unauthenticated users to login
login_manager.login_view = "login"

# set custom login message and category for flashing login required routes
login_manager.login_message = "Please login to continue."
login_manager.login_message_category = "error"


# reload user from session for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# user table
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # usernames need to be unique
    username = db.Column(db.String(80), unique=True, nullable=False)

    # store hashed password only
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        # hash the password before saving
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        # compare input password with stored hash
        return bcrypt.check_password_hash(self.password_hash, password)
    
# table for user favourite recipes
class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # recipe_id is TheMealDB id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    recipe_id = db.Column(db.String(20), nullable=False)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/countries")
def countries():
    message = None

    countries_list = get_countries()
    message = None if countries_list else "No countries returned from API"

    return render_template("countries.html", countries=countries_list, message=message)


@app.route("/recipes")
def recipes():
    # pull query params with safe defaults
    search = (request.args.get("search") or "").strip()
    region = (request.args.get("region") or "").strip()
    course = (request.args.get("course") or "all").strip().lower()

    meals = []
    message = None

    # search by meal name
    if search:
        meals = search_meals(search) or []

        if not meals:
            message = f"No Results found for: {search}"

    # otherwise filter by region
    elif region:
        meals = get_meals_by_region(region) or []

        if not meals:
            message = f"No Results found for: {region}"

    # empty search case
    elif "search" in request.args:
        message = "Please enter a search term"

    # optional dessert-only filter
    if course == "dessert" and meals:
        meals = [
            m for m in meals
            if (m.get("strCategory") or "").lower() == "dessert"
        ]

        if not meals:
            message = f"No Results found for: {search or region or 'dessert'}"

    return render_template(
        "recipes.html",
        meals=meals,
        region=region,
        search=search,
        course=course,
        message=message
    )


@app.route("/recipe/<recipe_id>")
def recipe_detail(recipe_id):
    
    try:       
        meal = get_meal_by_id(recipe_id)
        
        if not meal:
            return "Recipe not found", 404

        ingredients = []

        # API splits ingredients into indexed fields, so rebuild as a list
        for i in range(1, 21):
            ingredient = meal.get(f"strIngredient{i}")
            measure = meal.get(f"strMeasure{i}")

            # only add if ingredient actually exists
            if ingredient and ingredient.strip():
                ingredients.append(f"{measure} {ingredient}")
                
        saved = False

        # set favourite button state for logged-in users
        if current_user.is_authenticated:
            saved = Favourite.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first() is not None

        return render_template("recipe.html", meal=meal, ingredients=ingredients, saved=saved)

    except Exception:
        return "Error loading recipe", 500


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/add_favourite/<recipe_id>", methods=["POST"])
@login_required
def add_favourite(recipe_id):

    # avoid duplicate favourites
    existing = Favourite.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()

    if not existing:
        fav = Favourite(user_id=current_user.id, recipe_id=recipe_id)
        db.session.add(fav)
        db.session.commit()
        flash("Recipe added to favourites!", "success")

    return redirect(request.referrer or url_for("recipes"))


@app.route("/favourites")
@login_required
def favourites():
    
    # get all favourites for current user
    favs = Favourite.query.filter_by(user_id=current_user.id).all()
    
    meals = []
    
    for fav in favs:
        meal = get_meal_by_id(fav.recipe_id)
        if meal:
            meals.append(meal)
        
    return render_template("favourites.html", meals=meals)


@app.route("/remove_favourite/<recipe_id>", methods=["POST"])
@login_required
def remove_favourite(recipe_id):
    # find matching favourite for this user and recipe
    fav = Favourite.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()

    # delete only if it exists
    if fav:
        db.session.delete(fav)
        db.session.commit()
        
        if request.referrer and "favourites" in request.referrer:
            flash("Recipe removed from favourites!", "success")

    return redirect(request.referrer or url_for("favourites"))


# create account route (handles signup form + user creation)
@app.route("/auth/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        # get form input and clean it
        username = (request.form.get("username") or "").strip()
        password = (request.form.get("password") or "").strip()

        # basic validation so empty values do not get sent to database
        if not username or not password:
            flash("Username and password are required", "error")
            return render_template("auth/signup.html", username=username)

        # check if user already exists in database
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists", "error")
            return render_template("auth/signup.html", username=username)

        # create user object and hash password before saving
        new_user = User(username=username)
        new_user.set_password(password)

        # save user to database
        db.session.add(new_user)
        db.session.commit()
        
        flash("Account created successfully! Please log in.", "success")

        # send user to login after successful signup
        return redirect(url_for("login"))

    # show signup page (GET request)
    return render_template("auth/signup.html")


# login route (handles authentication + session creation)
@app.route("/auth/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        # get login input and clean it
        username = (request.form.get("username") or "").strip()
        password = (request.form.get("password") or "").strip()
        
        if not username or not password:
            flash("Username and password are required", "error")
            return render_template("auth/login.html", username=username)

        # look up user in database
        user = User.query.filter_by(username=username).first()

        # verify user exists and password matches hash
        if user and user.check_password(password):
            # log user in and create session cookie
            login_user(user)
            
            flash("Logged in successfully!", "success")

            # send to profile after successful login
            return redirect(url_for("profile"))

        # wrong credentials
        flash("Invalid username or password", "error")
        return render_template("auth/login.html", username=username)

    # show login page (GET request)
    return render_template("auth/login.html")


# log user out
@app.route("/auth/logout", methods=["POST"])
@login_required
def logout():
    # clear session
    logout_user()
    
    flash("Logged out successfully!", "success")
    
    return redirect(url_for("login"))


# profile page
@app.route("/auth/profile")
@login_required
def profile():
    
    # show total number of favourites for current user
    total = Favourite.query.filter_by(user_id=current_user.id).count()
    
    # show 3 most recently added favourites for current user
    favs = Favourite.query.filter_by(user_id=current_user.id).order_by(Favourite.id.desc()).limit(3).all()
    
    top3 = [] 
    
    for fav in favs:
        meal = get_meal_by_id(fav.recipe_id)
        if meal:
            top3.append(meal)
    
    return render_template("auth/profile.html", total=total, top3=top3)


# create database tables if not already created (globalgrub.db file in instance folder)
with app.app_context():
    db.create_all()

# run the app on port from environment or default to 5000, with debug off in production
if __name__ == "__main__":
    is_production = os.environ.get("FLASK_ENV") == "production"
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=not is_production)
