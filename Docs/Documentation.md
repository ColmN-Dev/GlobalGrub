# GlobalGrub Documentation

**Last updated:** April 2026

---

## Overview

GlobalGrub is a Flask web application I built for browsing recipes from around the world using TheMealDB API.

The project started as a frontend-focused idea and gradually evolved into a full-stack application with server-side rendering, search and filtering, user authentication, and a favourites system (still in progress).

---

## Project Development

### 1. Initial frontend version

The first version of the project was focused on frontend design:
- HTML, CSS, and JavaScript
- Responsive layout for recipe cards and pages
- Basic UI structure for browsing recipes

At this stage, the focus was mainly on design and layout rather than backend logic.

---

### 2. API handled with JavaScript (fetch + async)

Originally, I used JavaScript to handle API requests:
- `fetch()` calls to TheMealDB
- async/await for handling responses
- rendering recipe data directly in the browser

This worked but became harder to manage as the project grew because:
- frontend logic became messy
- API responses were inconsistent
- state handling across pages was limited

---

### 3. Moving to Flask backend (server-side rendering)

I moved API handling into Flask.

This improved the project by:
- centralising logic in the backend
- simplifying frontend code
- making routing and data handling more consistent
- using Jinja templates for dynamic pages

At this point, the project became a full Flask web application instead of a frontend API viewer.

---

### 4. Search, filtering and multi-page structure

I added:
- search by meal name
- filter by region/country
- filter by course type (all or desserts)

This required restructuring the `/recipes` route to use query parameters.

I also added:
- `/countries` page for browsing regions
- `/recipe/<id>` page for full recipe details
- ingredient parsing using API fields 1–20

---

### 5. Responsive design challenges

A large part of early development was UI work.

Problems included:
- recipe cards breaking on smaller screens
- navigation not scaling properly on mobile
- inconsistent spacing and layout across pages

These were fixed through repeated CSS adjustments.

---

### 6. Authentication system

Later in development, I added user authentication:

- user registration (signup)
- login and logout
- password hashing with Flask-Bcrypt
- session handling using Flask-Login
- SQLite database using SQLAlchemy

This changed the app from a public API viewer into a user-based system.

---

## Design Decisions

### Theme and visual direction

At the start, I planned a **warm forest-inspired theme with a day/night toggle**.

During development, I changed direction because:
- theme switching added unnecessary complexity
- it was harder to keep styling consistent
- it did not improve usability enough

I moved instead to a simpler design:

- warm restaurant / outdoor dining atmosphere
- inspired by evening dining and sunset lighting
- focus on food presentation rather than heavy theming

---

### Final UI style

The final design uses:
- dark glass-style UI (navbar, footer, cards, buttons)
- warm sunset-inspired background tones
- soft contrast between background and content

This keeps the site visually warm while staying readable and consistent.

---

### UI interactions

To improve usability and feel, I added:
- light grey hover effects on interactive elements
- `translateY()` lift effect on cards and buttons
- smooth CSS transitions for hover states

---

### Backend design choices

- Flask used for server-side rendering to keep the project simple
- Flask-Login used instead of custom authentication for security
- SQLite used because it is lightweight and easy to manage
- Jinja templates used instead of a frontend framework

---

### Routing approach

Instead of multiple pages for filtering, I used query parameters:
- `search`
- `region`
- `course`

This kept routing simpler and easier to maintain.

---

## Problems and Challenges

### 1. Switching from frontend API calls to Flask

The original version used JavaScript fetch calls, which caused:
- messy frontend logic
- inconsistent rendering
- difficulty managing API responses

Moving to Flask fixed this by centralising logic.

---

### 2. Responsive design issues

The UI required several iterations to fix:
- broken mobile layouts
- navigation scaling issues
- inconsistent spacing

---

### 3. Database setup issue

At one point I got:

> no such table: user

This happened because the database was not initialised.

Fix:
```python
with app.app_context():
    db.create_all()
```
---

### 4. Understanding authentication flow

It was initially unclear how Flask-Login works:

- how `current_user` works  
- why `user_loader` is required  
- how sessions persist between pages  

I learned that only the user ID is stored in the session. The full user object is then loaded again on each request using the `user_loader` function.

---

### 5. API inconsistency issues

TheMealDB API sometimes returns:

- empty results  
- missing fields  
- inconsistent structures  

These were handled using fallback checks and safe handling in Python so the app does not break when data is missing.

---

### 6. Code structure during development

Early versions mixed:

- API logic  
- authentication logic  
- route handling  

As the project grew, I separated the code into clearer sections so each part of the application has a defined responsibility.

---

## Current limitations

- Favourites system is not fully implemented  
- No flash messaging for login/signup feedback  
- Profile page is still basic and will be improved later  

---

## What I learned

- How Flask applications are structured  
- Difference between frontend and backend responsibilities  
- How authentication systems work in practice  
- How sessions work with Flask-Login  
- How to debug database and API issues  
- How design and structure improve through iteration  

---

## Credits

Authentication system structure was inspired by:

https://github.com/neupanic/Python-Flask-Authentication-Tutorial

Used for:
- Flask-Login setup  
- `user_loader` implementation  
- authentication flow  
- password hashing approach  

Adapted in this project by me:
- integrated into my own route structure and template layout  
- changed navigation/profile flow to match GlobalGrub pages  
- added my own validation handling for signup/login inputs  
- connected authentication to my existing recipe app architecture  