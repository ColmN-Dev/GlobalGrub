# GlobalGrub Documentation

**Last updated:** April 29, 2026

---

## Overview

GlobalGrub is a Flask web application I built for browsing recipes from around the world using TheMealDB API. The project started as a frontend-focused application and gradually developed into a full-stack Flask system with server-side rendering, authentication, database storage, and a favourites feature.

The development followed a step-by-step progression from UI design → API integration → backend structure → authentication → persistent user data.

---

## Project Development

### 1. Initial frontend version
I started the project using HTML, CSS, and JavaScript to build the UI, including recipe cards, navigation, and page structure.

---

### 2. JavaScript API integration
I originally used `fetch()` in JavaScript to pull data from TheMealDB API. This worked well early on but became harder to manage as the project grew due to:
- scattered API logic across files
- limited error handling
- duplicated logic between pages

---

### 3. Moving API logic to Flask backend
I moved all API requests into Flask routes. This allowed me to:
- centralise API handling
- simplify frontend templates using Jinja
- improve maintainability and structure

---

### 4. Helper module (helpers.py)
I created a `helpers.py` file to handle API logic separately from `app.py`.

It includes:
- `get_meal_by_id`
- `search_meals`
- `get_meals_by_region`
- `get_countries`

This helped me:
- remove API logic from routes
- keep `app.py` cleaner
- reuse functions across multiple routes

---

### 5. Search and filtering system
I implemented search and filtering using query parameters:
- `search` for meal name search
- `region` for country filtering
- `course` for dessert filtering

---

### 6. Authentication system
I implemented authentication using:
- Flask-Login
- Flask-Bcrypt
- SQLite with SQLAlchemy

This allowed me to:
- register users
- log in and log out users
- manage sessions securely
- hash passwords properly before storing them

Flask-Login handles route protection using `@login_required`, so I no longer needed manual authentication checks in every route.

---

### 7. Favourites system
I built a favourites system using a separate database table:

- `Favourite(user_id, recipe_id)`

This allows users to save recipes without storing full API data locally. I also made sure duplicates are prevented so the same recipe cannot be saved twice by the same user.

---

### 8. Profile system
I created a profile page that:
- shows total number of favourites
- displays the latest 3 saved recipes
- fetches full recipe details from the API using stored IDs

Since only recipe IDs are stored in the database, I fetch full recipe data when rendering the profile page.

---

### 9. Flash message system
I implemented flash messages using Flask’s `flash()` function to give users feedback across the app.

I used flash messages for:
- signup success and errors
- login success and errors
- logout confirmation
- adding favourites
- removing favourites
- access control redirects

#### Implementation details:
- I used categories: `success` and `error`
- I render flash messages globally in `base.html`
- I styled them using `.flash`, `.success`, and `.error`

#### Design decision:
I chose flash messages over inline form messages because it gives a consistent feedback system across the entire application.

Reference:
https://www.geeksforgeeks.org/python/flask-message-flashing/

---

### 10. Error handling
I implemented error handling using:
- `try/except` blocks for API calls  
- custom `404` and `500` error pages  
- Flask’s built-in error handling system  

Initially, I followed Flask’s decorator-based approach (`@app.errorhandler`), but I encountered circular import issues when separating error logic into a dedicated file.

Previously, `errors.py` imported the Flask app instance:
```python
from app import app
```

while `app.py` also imported `errors`, creating a circular dependency. This prevented the error handlers from being registered correctly and caused Flask to fall back to default error pages.

To resolve this, I refactored the error handlers into standalone functions and registered them in `app.py` using:

```python
app.register_error_handler(404, errors.not_found)
app.register_error_handler(500, errors.internal_error)
```

This removed the circular import and ensured that custom templates (`errors/404.html`, `errors/500.html`) are rendered correctly.

Reference:
https://flask.palletsprojects.com/en/stable/errorhandling/

---

### 11. JavaScript enhancements
I added JavaScript features to improve usability:
- mobile hamburger menu toggle
- password visibility toggle
- loading spinner for recipe searches
- ARIA attribute updates for accessibility

Reference:
https://www.geeksforgeeks.org/javascript/show-hide-password-using-javascript/

---

## Design Decisions

### UI direction
I originally planned a forest-style theme but changed it to a warm restaurant-style design to better suit food presentation and improve consistency.

---

### Routing approach
I used a single `/recipes` route with query parameters instead of multiple routes. This made filtering simpler and more flexible.

---

### Database design
I used SQLAlchemy with `db.create_all()` instead of migrations to keep the setup simple for the assignment scope.

Reference:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

---

## Problems and Challenges

### 1. API to backend migration
I moved API logic from frontend JavaScript into Flask to improve structure and maintainability.

Reference:
https://www.geeksforgeeks.org/python/flask-tutorial/

---

### 2. Refactoring into helpers.py
I extracted API logic into a helper file to improve:
- code organisation
- reusability
- readability of routes

---

### 3. Authentication understanding
I had to understand:
- sessions
- `current_user`
- Flask-Login lifecycle

Reference:
https://github.com/neupanic/Python-Flask-Authentication-Tutorial

---

### 4. Route protection
I replaced manual authentication checks with `@login_required` for cleaner route protection.

---

### 5. Database initialization issue
I fixed a `no such table` error by ensuring `db.create_all()` runs inside the Flask app context.

---

### 6. API inconsistencies
The API sometimes returned missing or incomplete data, so I handled this using:
- `.get()` safe access
- fallback values
- route-level validation

Reference:
https://www.geeksforgeeks.org/python/response-raise_for_status-python-requests/

---

### 7. Favourites system complexity
The main challenge was linking:
- external API data
- local database storage

I solved this by storing only `recipe_id` and fetching full data when needed.

---

### 8. Profile rendering issue
The profile initially showed raw IDs, so I updated it to fetch full meal data from the API.

---

### 9. Layout inconsistencies
I fixed inconsistent UI styling by standardising card components and CSS structure.

---

### 10. Deployment cold start
Render free tier caused delays, so I used a cron-job ping every 10 minutes to keep the service active as it shuts down after 15 minutes of inactivity.

---

### 11. Circular import issue (error handling)
When separating error handling into `errors.py`, I encountered a circular import between `app.py` and `errors.py`. This prevented the error handlers from being registered correctly, causing Flask to fall back to its default error pages.

I resolved this by:
- removing the dependency on the Flask app instance from `errors.py`  
- converting error handlers into standalone functions  
- registering them in `app.py` using `app.register_error_handler`  

This improved the structure of the application and avoided import-related issues.

---

## Current limitations

- API calls for favourites are not cached
- No frontend form validation yet
- Error handling is implemented but does not include logging or advanced monitoring

---

## Future improvements

- Add password strength validation using regex
- Potentially introduce Flask-Migrate for future schema changes

---

## What I learned

I learned how to build a full Flask application with routing, authentication, database integration, and API handling. I also learned how to structure a project properly by separating concerns using helper modules and improving maintainability over time.

---

## Credits

### Authentication system
https://github.com/neupanic/Python-Flask-Authentication-Tutorial

### Database & Flask structure
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database  
https://www.geeksforgeeks.org/python/connect-flask-to-a-database-with-flask-sqlalchemy/  
https://www.geeksforgeeks.org/python/flask-tutorial/

### JavaScript
https://www.geeksforgeeks.org/javascript/show-hide-password-using-javascript/

### API handling
https://www.geeksforgeeks.org/python/response-raise_for_status-python-requests/

### Flask error handling
https://flask.palletsprojects.com/en/stable/errorhandling/

### Flash messages
https://www.geeksforgeeks.org/python/flask-message-flashing/