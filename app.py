from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.secret_key = 'globalgrub-dev-key'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/recipes")
def recipes():
    search = (request.args.get("search") or "").strip()
    region = (request.args.get("region") or "").strip()
    
    meals = []
    message = None

    try:
        # Empty search term
        if "search" in request.args and search == "":
            message = "Please enter a search term."
        
        # Search by name
        elif search:
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={search}"
            response = requests.get(url, timeout=10)
            data = response.json()
            meals = data.get("meals") or []
            
            if not meals:
                message = f"No results found for: {search}"

        # Filter by region
        elif region:
            url = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={region}"
            response = requests.get(url, timeout=10)
            data = response.json()
            meals = data.get("meals") or []
            
            if not meals:
                message = "No results found."

    except requests.exceptions.RequestException:
        message = "Could not connect to the recipe database. Please try again later."
    except Exception:
        message = "Something went wrong. Please try again."

    return render_template("recipes.html", meals=meals, region=region, search=search, message=message)

@app.route("/recipe/<id>")
def recipe_detail(id):
    try:
        url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if not data.get("meals"):
            return "Recipe not found", 404

        meal = data["meals"][0]

        # Extract ingredients
        ingredients = []
        for i in range(1, 21):
            ingredient = meal.get(f"strIngredient{i}")
            measure = meal.get(f"strMeasure{i}")
            if ingredient and ingredient.strip():
                ingredients.append(f"{measure} {ingredient}")

        return render_template("recipe.html", meal=meal, ingredients=ingredients)

    except Exception:
        return "Could not load recipe. Please try again later.", 500

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/favourites")
def favourites():
    return render_template("favourites.html")

@app.route("/auth/signup")
def signup():
    return render_template("/auth/signup.html")

@app.route("/auth/login")
def login():
    return render_template("/auth/login.html")

@app.route("/auth/profile")
def profile():
    return render_template("/auth/profile.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
