# GlobalGrub

Last updated: April 12, 2026

## GitHub Repository

https://github.com/ColmN-Dev/GlobalGrub

## Live Site

https://globalgrub-tsyf.onrender.com

---

## Overview

GlobalGrub is a Flask web app for discovering recipes from around the world using TheMealDB API. Users can browse by country, search by meal name, and open a full recipe details page with ingredients and instructions.

---

## Current Features

- Home page with hero section, marquee, and region cards
- Countries page that lists all available MealDB countries (A-Z)
- Recipe browsing by region (`/recipes?region=...`)
- Recipe search by name (`/recipes?search=...`)
- Simple search filter buttons: `All` and `Dessert`
- Dessert filter is applied to search results
- Recipe detail page (`/recipe/<id>`) with ingredients, instructions, and media data when available
- Responsive layout with desktop navbar and mobile menu
- Accessibility improvements (image alt text, ARIA labels, and iframe title)
- About, Favourites, Login, Signup, and Profile pages (template routes)

---

## Tech Stack

- Backend: Python, Flask
- API: TheMealDB
- Frontend: HTML, Jinja templates, CSS, JavaScript
- Deployment: Render (Gunicorn)

---

## Project Structure

- `app.py`
- `templates/`
- `templates/auth/`
- `static/css/`
- `static/js/`
- `static/images/`
- `static/images/wireframes/`
- `Docs/`

---

## Local Setup

1. Create and activate a virtual environment.
2. Install requirements:
	- `pip install -r requirements.txt`
3. Run the app:
	- `python app.py`
4. Open:
	- `http://127.0.0.1:5000`

---

## Future Improvements

- Full authentication flow (register/login/logout sessions)
- Persistent favourites storage
- User profile persistence
- Additional filters and sorting options

---

## Status

In development as part of a Python module assignment.
