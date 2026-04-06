from flask import Flask, render_template
app = Flask(__name__)

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
