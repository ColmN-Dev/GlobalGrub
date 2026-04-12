from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.secret_key = 'globalgrub-dev-key'

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
        
        # Remove empty values and sort A-Z
        countries_list = sorted(
            [item.get("strArea", "") for item in (data.get("meals") or []) if item.get("strArea")],
            key=str.lower
        )

        if not countries_list:
            message = "No countries available right now. Please try again later."

    except requests.exceptions.RequestException:
        message = "Could not connect to the recipe database. Please try again later."
    except Exception:
        message = "Something went wrong. Please try again."

    return render_template("countries.html", countries=countries_list, message=message)

@app.route("/recipes")
def recipes():
    # Read query values from URL
    search = (request.args.get("search") or "").strip()
    region = (request.args.get("region") or "").strip()
    course = (request.args.get("course") or "all").strip().lower()
    
    meals = []
    message = None

    try:
        # Show message only when user submits an empty search
        if "search" in request.args and search == "" and not region:
            message = "Please enter a search term."
        
        elif search:
            # Search by meal name
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={search}"
            response = requests.get(url, timeout=10)
            data = response.json()
            meals = data.get("meals") or []

            # Optional course filter for search results
            if course == "dessert":
                meals = [meal for meal in meals if (meal.get("strCategory") or "").lower() == "dessert"]
            
            if not meals:
                message = f"No results found for: {search}"

        elif region:
            # Filter recipes by country/region
            url = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={region}"
            response = requests.get(url, timeout=10)
            data = response.json()
            meals = data.get("meals") or []

            # Optional course filter for region results
            if course == "dessert":
                meals = [meal for meal in meals if (meal.get("strCategory") or "").lower() == "dessert"]
            
            if not meals:
                message = "No results found."

    except requests.exceptions.RequestException:
        # API/network issue
        message = "Could not connect to the recipe database. Please try again later."
    except Exception:
        message = "Something went wrong. Please try again."

    return render_template("recipes.html", meals=meals, region=region, search=search, course=course, message=message)

@app.route("/recipe/<id>")
def recipe_detail(id):
    try:
        # Load full meal details by id
        url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}"
        response = requests.get(url, timeout=10)
        data = response.json()

        # Stop early if meal does not exist
        if not data.get("meals"):
            return "Recipe not found", 404

        meal = data["meals"][0]

        # Build ingredient list from fields 1 to 20
        ingredients = []
        for i in range(1, 21):
            ingredient = meal.get(f"strIngredient{i}")
            measure = meal.get(f"strMeasure{i}")
            if ingredient and ingredient.strip():
                ingredients.append(f"{measure} {ingredient}")

        return render_template("recipe.html", meal=meal, ingredients=ingredients)

    except Exception:
        # Fallback error if detail page cannot load
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
