# GlobalGrub

**Last updated:** April 29, 2026

---

## Repository and Live App

- GitHub: https://github.com/ColmN-Dev/GlobalGrub

- Live site: https://globalgrub-tsyf.onrender.com  

---

## Overview

GlobalGrub is a Flask web application I built to browse recipes from around the world using TheMealDB API. The app focuses on server-side rendering, clean routing, and a structured backend, while keeping frontend JavaScript minimal and purposeful.

Users can search for recipes, filter by region, view detailed meal information, and save favourites through an authenticated account system.

---

## Key Features

- Server-rendered Flask application using Jinja templates  
- Recipe search and region-based filtering  
- Detailed recipe pages with dynamically built ingredient lists  
- User authentication system (signup, login, logout)  
- Favourite recipes system stored in SQLite  
- Flash message feedback for user actions (login, signup, favourites)  
- Profile page showing saved recipes and recent activity  
- Responsive design with mobile navigation  
- Accessibility improvements using ARIA attributes  
- Lazy-loaded images for performance optimisation  

---

## Tech Stack

- **Backend:** Python, Flask  
- **Database:** SQLite (Flask-SQLAlchemy)  
- **Authentication:** Flask-Login, Flask-Bcrypt  
- **Frontend:** HTML, Jinja, CSS, JavaScript  
- **API:** TheMealDB  
- **Environment config:** python-dotenv (`.env`)  
- **Deployment:** Render (Gunicorn)  

---

## Project Structure

```

GlobalGrub/
│
├── app.py                # Main Flask application (routes, auth, logic)
├── helpers.py            # API helper functions (TheMealDB integration)
├── templates/            # Jinja templates
│   └── auth/             # Authentication templates
├── static/
│   ├── css/style.css     # Styling
│   └── js/script.js      # JavaScript functionality
├── Docs/Documentation.md # Full project documentation
└── requirements.txt

```

---

## Local Development Setup

1. Create virtual environment:

```powershell
python -m venv venv
```

2. Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Create `.env` file:

```env
SECRET_KEY=your_secret_key_here
```

5. Run the app:

```powershell
python app.py
```

6. Open in browser:

```
http://127.0.0.1:5000
```

---

## Deployment (Render)

The app is deployed using a Render Web Service with:

* **Build command:**
  `pip install -r requirements.txt`

* **Start command:**
  `gunicorn app:app`

To reduce cold start delays on the free tier, a cron job is used to periodically ping the service.

---

## Notes

* SQLite database is automatically created in the `instance/` folder
* Tables are created at runtime using `db.create_all()`
* Authentication routes are grouped under `/auth/`

---

## Current Limitations

* Favourites require multiple API calls
* No frontend form validation yet
* No custom error pages implemented yet

---

## Planned Improvements

* Add regex-based password validation
* Implement custom 404 and 500 error pages
* Expand UI feedback and validation

---

## Attribution

This project was built using learning resources which were adapted into a custom implementation:

* [https://github.com/neupanic/Python-Flask-Authentication-Tutorial](https://github.com/neupanic/Python-Flask-Authentication-Tutorial)
* [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
* [https://www.geeksforgeeks.org/python/connect-flask-to-a-database-with-flask-sqlalchemy/](https://www.geeksforgeeks.org/python/connect-flask-to-a-database-with-flask-sqlalchemy/)
* [https://www.geeksforgeeks.org/python/flask-tutorial/](https://www.geeksforgeeks.org/python/flask-tutorial/)
* [https://www.geeksforgeeks.org/javascript/show-hide-password-using-javascript/](https://www.geeksforgeeks.org/javascript/show-hide-password-using-javascript/)
* [https://www.geeksforgeeks.org/python/response-raise_for_status-python-requests/](https://www.geeksforgeeks.org/python/response-raise_for_status-python-requests/)
* [https://flask.palletsprojects.com/en/stable/errorhandling/](https://flask.palletsprojects.com/en/stable/errorhandling/)
* [https://www.geeksforgeeks.org/python/flask-message-flashing/](https://www.geeksforgeeks.org/python/flask-message-flashing/)

---

## Assignment Status

This project is currently in active development as part of a Python Flask module assignment.

---



 
