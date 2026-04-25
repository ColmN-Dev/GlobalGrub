# GlobalGrub

Last updated: April 25, 2026

## Repository and Live App

- GitHub: https://github.com/ColmN-Dev/GlobalGrub
- Live site: https://globalgrub-tsyf.onrender.com

## Overview

GlobalGrub is a Flask web application for browsing international recipes using TheMealDB API. The app includes server-side rendering with Jinja templates, recipe search and filter features, user authentication with Flask-Login, and a favourites system backed by SQLite.

## Key Features

- Multi-page Flask app with route-based navigation
- Countries page with A-Z list of MealDB regions
- Recipe browsing by region
- Recipe name search with optional dessert filter
- Recipe detail page with parsed ingredient list
- User signup, login, logout, and profile page
- Add/remove favourite recipes for logged-in users
- Favourites page showing all saved recipes
- Password hashing with Flask-Bcrypt
- SQLite user and favourites persistence via Flask-SQLAlchemy
- Responsive layout with desktop navbar and mobile hamburger menu
- Cron job configured to keep Render service warm and avoid cold start delays
- Loading spinner on recipes page during search requests
- Dynamic ARIA attribute updates via JavaScript for accessible interactive elements

## Tech Stack

- Backend: Python, Flask
- Database: SQLite (via Flask-SQLAlchemy)
- Auth: Flask-Login, Flask-Bcrypt
- Frontend: HTML, Jinja, CSS, JavaScript
- API: TheMealDB
- Environment config: python-dotenv (`.env`)
- Hosting: Render (Gunicorn)

## Project Structure

- `app.py`
- `templates/`
- `templates/auth/`
- `static/css/style.css`
- `static/js/script.js`
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

4. Create a `.env` file in project root:

```env
SECRET_KEY=your_long_random_secret_here
```

5. Run the app:

```powershell
python app.py
```

6. Open in browser:

`http://127.0.0.1:5000`

## Notes

- The SQLite database file is created in the Flask `instance/` folder (`instance/globalgrub.db`).
- Tables are created automatically at startup using `db.create_all()`.
- Auth routes are prefixed under `/auth/` (e.g. `/auth/login`, `/auth/profile`).

## Deployment (Render)

Current deployment uses Render Web Service with:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

## Current Limitations

- Favourites are fetched from the API one by one per request and could be optimised later
- No frontend form validation yet — planned for next development phase
- No custom error pages yet — a `404.html` and general error handling are planned next

## Planned Next Steps

- Flash messages for login, signup, and favourites feedback
- Frontend and backend form validation with regex for password strength
- Custom `404.html` and error page handling to avoid blank pages on crashes

## Attribution

Authentication flow was inspired by:

https://github.com/neupanic/Python-Flask-Authentication-Tutorial

Implementation was adapted to this project's route structure, templates, and validation flow.

## Assignment Status

In active development for a Python Flask module assignment.