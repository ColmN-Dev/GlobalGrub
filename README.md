# GlobalGrub

Last updated: April 25, 2026

## Repository and Live App

- GitHub: https://github.com/ColmN-Dev/GlobalGrub
- Live site: https://globalgrub-tsyf.onrender.com

## Overview

GlobalGrub is a Flask web application for browsing international recipes using TheMealDB API. The app includes server-side rendering with Jinja templates, recipe search and filter features, user authentication with Flask-Login, and a favourites system backed by SQLite.

## Key Features

- Multi-page Flask application with structured route-based navigation  
- Browse recipes by region using TheMealDB (A–Z country listing)  
- Recipe search with optional dessert filtering  
- Detailed recipe view with dynamically parsed ingredient list  
- Full authentication system (signup, login, logout, profile) using Flask-Login  
- Favourite recipes system with persistent storage via Flask-SQLAlchemy (SQLite)  
- Secure password hashing using Flask-Bcrypt  
- Responsive UI with desktop navigation and mobile hamburger menu  
- Loading spinner with dynamic ARIA updates for accessible async interactions  
- Lazy loading on images to improve performance and reduce initial load time  
- Environment-aware configuration for development and production (debug, port handling)  
- Deployed with Gunicorn and a cron job to prevent cold starts on Render  

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