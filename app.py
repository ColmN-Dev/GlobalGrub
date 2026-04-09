from flask import Flask, render_template
import requests

app.secret_key = 'globalgrub-dev-key'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home")
def home_alias():
    return render_template("home.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

@app.route("/recipe/<id>")
def recipe_detail(id):
    res = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
    data = res.json()

    if not data["meals"]:
        return "Recipe not found", 404

    meal = data["meals"][0]

    return render_template("recipe.html", meal=meal)



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
