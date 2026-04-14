from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import requests

# basic flask setup
app = Flask(__name__)

# needed for sessions (login cookies etc)
app.secret_key = 'globalgrub-dev-key'

# sqlite db for storing users
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///globalgrub.db'
db = SQLAlchemy(app)

# used for hashing passwords so they aren't stored in plain text
bcrypt = Bcrypt(app)

# flask-login setup (handles login sessions)
login_manager = LoginManager()
login_manager.init_app(app)

# if user is not logged in, send them to login page
login_manager.login_view = 'login'


# user table for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # usernames must be unique
    username = db.Column(db.String(80), unique=True, nullable=False)

    # stored hashed password (never store raw password)
    password_hash = db.Column(db.String(128), nullable=False)

    # hash password before saving user
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # check if entered password matches stored hash
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/countries")
def countries():
    countries_list = []
    message = None

    try:
        # call external API for regions
        url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
        response = requests.get(url, timeout=10)
        data = response.json()

        # clean up list and sort alphabetically
        countries_list = sorted(
            [item.get("strArea", "") for item in (data.get("meals") or []) if item.get("strArea")],
            key=str.lower
        )

        if not countries_list:
            message = "no countries returned from API"

    except requests.exceptions.RequestException:
        message = "API request failed"
    except Exception:
        message = "An error occurred while processing your request"

    return render_template("countries.html", countries=countries_list, message=message)


@app.route("/recipes")
def recipes():
    search = (request.args.get("search") or "").strip()
    region = (request.args.get("region") or "").strip()
    course = (request.args.get("course") or "all").strip().lower()

    meals = []
    message = None

    try:
        # if user submits empty search
        if "search" in request.args and search == "" and not region:
            message = "Please enter something to search"

        elif search:
            # search by meal name
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={search}"
            response = requests.get(url, timeout=10)
            data = response.json()
            meals = data.get("meals") or []

            # optional filter for desserts only
            if course == "dessert":
                meals = [meal for meal in meals if (meal.get("strCategory") or "").lower() == "dessert"]

            if not meals:
                message = f"no results for {search}"

        elif region:
            # filter by region
            url = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={region}"
            response = requests.get(url, timeout=10)
            data = response.json()
            meals = data.get("meals") or []

            if course == "dessert":
                meals = [meal for meal in meals if (meal.get("strCategory") or "").lower() == "dessert"]

            if not meals:
                message = "No results found"

    except requests.exceptions.RequestException:
        message = "API request failed"
    except Exception:
        message = "An error occurred while processing your request"

    return render_template(
        "recipes.html",
        meals=meals,
        region=region,
        search=search,
        course=course,
        message=message
    )


@app.route("/recipe/<id>")
def recipe_detail(id):
    try:
        # get full recipe info
        url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if not data.get("meals"):
            return "Recipe not found", 404

        meal = data["meals"][0]

        # build ingredient list
        ingredients = []
        for i in range(1, 21):
            ingredient = meal.get(f"strIngredient{i}")
            measure = meal.get(f"strMeasure{i}")

            if ingredient and ingredient.strip():
                ingredients.append(f"{measure} {ingredient}")

        return render_template("recipe.html", meal=meal, ingredients=ingredients)

    except Exception:
        return "Error loading recipe", 500


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/favourites")
@login_required
def favourites():
    return render_template("favourites.html")


@app.route("/auth/signup", methods=["GET", "POST"])
def signup():
    return render_template("/auth/signup.html")


@app.route("/auth/login", methods=["GET", "POST"])
def login():
    return render_template("/auth/login.html")


@app.route("/auth/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/auth/profile")
@login_required
def profile():
    return render_template("/auth/profile.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)