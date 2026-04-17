from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import requests
import os

# load variables from .env into the environment (for local development)
load_dotenv()

# initialize Flask app
app = Flask(__name__)

# config for sessions/cookies and database
# require SECRET_KEY from environment/.env
app.secret_key = os.environ["SECRET_KEY"]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///globalgrub.db'

# initialize database and password hashing
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# setup login system
login_manager = LoginManager()
login_manager.init_app(app)

# send user here if they try access something without being logged in
login_manager.login_view = 'login'


# this is used by flask-login to reload the user from session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# user table
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # usernames need to be unique
    username = db.Column(db.String(80), unique=True, nullable=False)

    # store hashed password, never the actual one for security purposes
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        # hash the password before saving
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        # compare input password with stored hash
        return bcrypt.check_password_hash(self.password_hash, password)
    
# table to store user favourites
class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # store user id and recipe id for each favourite, recipe id is string from API
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    recipe_id = db.Column(db.String(20), nullable=False)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/countries")
def countries():
    countries_list = []
    message = None

    try:
        url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"

        response = requests.get(url, timeout=10)
        data = response.json()

        # pull country names out of API response and sort them
        countries_list = sorted(
            [item.get("strArea", "") for item in (data.get("meals") or []) if item.get("strArea")],
            key=str.lower
        )

        if not countries_list:
            message = "No countries returned from API"

    except requests.exceptions.RequestException:
        message = "API request failed"
    except Exception:
        message = "An error occurred"

    return render_template("countries.html", countries=countries_list, message=message)


@app.route("/recipes")
def recipes():
    # grab values from URL, default to empty so nothing breaks
    search = (request.args.get("search") or "").strip()
    region = (request.args.get("region") or "").strip()
    course = (request.args.get("course") or "all").strip().lower()

    meals = []
    message = None

    try:
        # user clicked search but didn’t type anything
        if "search" in request.args and search == "" and not region:
            message = "Please enter something to search"

        # search by meal name
        elif search:
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={search}"

            response = requests.get(url, timeout=10)
            data = response.json()

            # API sometimes returns None, so force it into a list
            meals = data.get("meals") or []

            # if dessert filter is selected, narrow results down
            if course == "dessert":
                meals = [
                    m for m in meals
                    if (m.get("strCategory") or "").lower() == "dessert"
                ]

            if not meals:
                message = f"No Results found for: {search}"

        # filter by region instead
        elif region:
            url = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={region}"

            response = requests.get(url, timeout=10)
            data = response.json()

            meals = data.get("meals") or []

            if not meals:
                message = f"No Results found for: {region}"

    except requests.exceptions.RequestException:
        message = "API request failed"
    except Exception:
        message = "An error occurred"

    return render_template(
        "recipes.html", meals=meals, region=region, search=search, course=course, message=message)


@app.route("/recipe/<id>")
def recipe_detail(id):
    try:
        # get full recipe details using meal id
        url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}"

        response = requests.get(url, timeout=10)
        data = response.json()

        if not data.get("meals"):
            return "Recipe not found", 404

        meal = data["meals"][0]

        ingredients = []

        # API splits ingredients across 20 fields so rebuild them into a list
        for i in range(1, 21):
            ingredient = meal.get(f"strIngredient{i}")
            measure = meal.get(f"strMeasure{i}")

            # only add if ingredient actually exists
            if ingredient and ingredient.strip():
                ingredients.append(f"{measure} {ingredient}")
                
        saved = False

        # if user is logged in, check if recipe is in their favourites to show correct button state for that recipe
        if current_user.is_authenticated:
            saved = Favourite.query.filter_by(user_id=current_user.id, recipe_id=id).first() is not None

        return render_template("recipe.html", meal=meal, ingredients=ingredients, saved=saved)

    except Exception:
        return "Error loading recipe", 500


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/add_favourite/<recipe_id>", methods=["POST"])
@login_required
def add_favourite(recipe_id):

    # check if this recipe is already in user's favourites to avoid duplicates using .first() to return one result
    existing = Favourite.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()

    if not existing:
        fav = Favourite(user_id=current_user.id, recipe_id=recipe_id)
        db.session.add(fav)
        db.session.commit()

    return redirect(request.referrer or url_for("recipes"))


@app.route("/favourites")
@login_required
def favourites():
    
    # search for all favourites that match the current user's id, .all() to return list of results
    favs = Favourite.query.filter_by(user_id=current_user.id).all()
    
    meals = []
    
    for fav in favs:
        url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={fav.recipe_id}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("meals"):
            meals.append(data["meals"][0])
        
    
    return render_template("favourites.html", meals=meals)


@app.route("/remove_favourite/<recipe_id>", methods=["POST"])
@login_required
def remove_favourite(recipe_id):

        # find the favourite entry for this user and recipe, .first() since there should only be one
        fav = Favourite.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()
        
        # if it exists, delete it from the database
        if fav:
            db.session.delete(fav)
            db.session.commit()

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
            return "Username and password are required", 400

        # check if user already exists in database
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Username already exists", 400

        # create user object and hash password before saving
        new_user = User(username=username)
        new_user.set_password(password)

        # save user to database
        db.session.add(new_user)
        db.session.commit()

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
            return "Username and password are required", 400

        # look up user in database
        user = User.query.filter_by(username=username).first()

        # verify user exists and password matches hash
        if user and user.check_password(password):
            # log user in and create session cookie
            login_user(user)

            # send to profile after successful login
            return redirect(url_for("profile"))

        # wrong credentials
        return "Invalid username or password", 401

    # show login page (GET request)
    return render_template("auth/login.html")


# log user out
@app.route("/auth/logout", methods=["POST"])
@login_required
def logout():
    # clear session
    logout_user()
    return redirect(url_for("login"))


# profile page
@app.route("/auth/profile")
@login_required
def profile():
    
    favs = Favourite.query.filter_by(user_id=current_user.id).all()
    
    total = len(favs)
    top3 = favs[:3]
    
    return render_template("auth/profile.html", total=total, top3=top3)


# create database tables if not already created (globalgrub.db file in instance folder)
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)