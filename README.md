# GlobalGrub

Last updated: April 15, 2026

## Repository and Live App

- GitHub: https://github.com/ColmN-Dev/GlobalGrub
- Live site: https://globalgrub-tsyf.onrender.com

## Overview

GlobalGrub is a Flask web application for browsing international recipes using TheMealDB API. The app includes server-side rendering with Jinja templates, recipe search/filter features, and user authentication with Flask-Login.

## Key Features

- Multi-page Flask app with route-based navigation
- Countries page with A-Z MealDB regions
- Recipe browsing by region
- Recipe name search with optional dessert filter
- Recipe detail page with ingredient parsing
- User signup, login, logout, and profile page
- Password hashing with Flask-Bcrypt
- SQLite user persistence via Flask-SQLAlchemy
- Responsive layout (desktop navbar and mobile menu)

## Tech Stack

- Backend: Python, Flask
- Database: SQLite (via Flask-SQLAlchemy)
- Auth: Flask-Login, Flask-Bcrypt
- Frontend: HTML, Jinja, CSS, JavaScript
- API: TheMealDB
- Hosting: Render (Gunicorn)

## Project Structure

- `app.py`
- `templates/`
- `templates/auth/`
- `static/css/style.css`
- `static/js/main.js`
- `static/js/search.js`
- `Docs/Documentation.md`

## Local Development Setup

1. Create virtual environment:

```powershell
python -m venv venv
```

2. Activate virtual environment (Windows PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run the app:

```powershell
python app.py
```

5. Open in browser:

`http://127.0.0.1:5000`

## Notes

- The SQLite database file is created in the Flask `instance/` folder (`instance/globalgrub.db`).
- Tables are created automatically at startup using `db.create_all()`.

## Deployment (Render)

Current deployment uses Render Web Service with:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

## Current Limitations

- Favourites page is still in progress
- Profile page works but is still basic

## Attribution

Authentication flow was inspired by:

https://github.com/neupanic/Python-Flask-Authentication-Tutorial

Implementation was adapted to this project's route structure, templates, and validation flow.

## Assignment Status

In active development for a Python Flask module assignment.
