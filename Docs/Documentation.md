
# GlobalGrub Documentation

**Last updated:** April 23, 2026

---

## Overview

GlobalGrub is a Flask web application built for browsing recipes from around the world using TheMealDB API.

The project started as a mainly frontend-focused build with some early backend ideas, and later developed into a full-stack application with Flask routes, database storage, user authentication, and a favourites system.

The main development focus moved step-by-step from UI design -> API integration -> backend structure -> user accounts and saved data.

---

## Project Development

### 1. Initial frontend-focused version (with early backend ideas)

The project started mainly on the frontend side using:
- HTML
- CSS
- JavaScript

At this stage, the focus was:
- page layout and design
- recipe card UI
- navigation between pages
- basic structure for future backend features

There was already an idea of using Flask later, but most of the early work was frontend.

---

### 2. Using JavaScript fetch for API

I originally used `fetch()` in JavaScript to get data from TheMealDB API.

This worked because:
- I was familiar with JavaScript from a previous project
- it was quick to set up
- it allowed recipes to load directly in the browser

However, issues appeared as the project grew:
- frontend logic became messy
- API handling was spread across files
- error handling was limited
- difficult to manage data across multiple pages

---

### 3. Moving API logic to Flask backend

I moved API requests into Flask routes.

This improved the project by:
- centralising API logic in the backend
- simplifying frontend JavaScript
- making data handling more consistent
- using Jinja templates for rendering pages

At this point, the project became a full Flask web application.

---

### 4. Search and filtering system

I added:
- search by meal name
- filter by region/country
- filter by course type (all or desserts)

This was handled using query parameters in Flask:
- `search`
- `region`
- `course`

Using query parameters kept the routing flexible and simple.

---

### 5. Error handling improvements

After building the main routes, I added error handling.

This included:
- `try/except` blocks around API calls
- timeout handling (`timeout=10`)
- safe fallback values when API returns empty data

This was needed because the API sometimes:
- returns empty results
- is slow to respond
- returns missing fields

---

### 6. Authentication system

Later in the project I added user accounts using:
- Flask-Login
- Flask-Bcrypt
- SQLite database (SQLAlchemy)

This allowed:
- user registration
- login/logout
- session-based authentication
- secure password storage (hashing)

I learned that Flask-Login:
- stores only the user ID in the session
- reloads the full user from the database on each request

---

### 7. Profile route and profile page

I added a dedicated profile route and connected it to a new profile UI.

Backend additions included:
- counting total saved favourites for the logged-in user
- selecting the latest saved favourites
- fetching full meal details from TheMealDB for display

Frontend additions included:
- profile header with user information
- total saved recipes summary
- top 3 recent favourite recipe cards
- quick actions (view all favourites and logout)

This was important because favourites in the database only store recipe IDs, so the profile page needed extra route logic to transform IDs into full recipe data before rendering.

---

## Design Decisions

### Theme choice

I originally planned a forest-style theme with a day/night toggle.

I changed this because:
- it added unnecessary complexity
- it made styling harder to keep consistent
- it did not improve usability much

I instead chose:
- a warm restaurant / evening dining style
- soft dark UI elements
- focus on food presentation

---

### UI design choices

To improve usability I added:
- hover effects on cards and buttons
- smooth CSS transitions
- consistent spacing and layout rules

These were added gradually during development.

---

### Backend choices

- Flask used for backend logic and routing
- SQLite used for simple local database storage
- Jinja templates used instead of frontend frameworks
- Flask-Login used for authentication instead of custom login system

These choices were made to keep the project simple and manageable.

---

### Routing approach

Instead of creating many separate pages, I used one main route:
- `/recipes`

Filtering is handled using query parameters.

This made the system:
- easier to manage
- more flexible
- easier to extend later

---

### Database design (`query.filter_by`)

I used `query.filter_by()` in SQLAlchemy to retrieve specific data from the database.

For example:
- finding favourites for a specific user
- checking if a recipe is already saved

This is useful because:
- it allows filtering by column values easily
- it keeps code readable
- it avoids writing raw SQL

This was important for the favourites system because each user must only see their own saved recipes.

---

## Problems and Challenges

### 1. Frontend -> backend migration

Issue: API calls were spread across frontend JavaScript and became hard to maintain.
Cause: As the app grew, search, filtering, and error handling were split across multiple files.
Fix: I moved API logic into Flask routes and rendered the data through Jinja templates so the flow stayed in one place.

---

### 2. Understanding authentication

Issue: Authentication flow was unclear at first.
Cause: I needed to understand sessions, `current_user`, `user_loader`, and how Flask-Login rebuilds the user on each request.
Fix: I mapped the full login lifecycle and aligned the routes with Flask-Login's session model.

---

### 3. Route protection change (guest -> login_required)

Issue: The first idea was to let guests open the favourites page and show a login message.
Cause: Mixed guest and authenticated behavior made the route logic more complicated than it needed to be.
Fix: I switched to `@login_required`, which kept the route cleaner and ensured only logged-in users could access saved data.

---

### 4. Database issue

Issue: I hit `no such table: user` during authentication testing.
Cause: The database tables had not been initialized in the active app context, so the models existed in code but not in SQLite.
Fix: I made sure `db.create_all()` runs inside `app.app_context()` so the tables are created when the app starts.

---

### 5. API reliability issues

Issue: TheMealDB responses were sometimes empty, partial, or inconsistent.
Cause: External API reliability varies across endpoints and some fields are missing depending on the meal.
Fix: I used safe `.get()` lookups, fallback defaults, and route-level error handling to keep the pages from breaking.

---

### 6. Favourites system and database relationships (major challenge)

Issue: Linking users, favourites, and API recipes was the most complex part of the project.
Cause: Recipe data comes from TheMealDB, but the app only stores `recipe_id` locally, so the database and API had to be coordinated carefully.
Fix: I created a separate `Favourite` model, added add/remove/query routes, and used user-scoped `filter_by()` checks so each user only sees and changes their own saved recipes.

---

### 7. Profile data mismatch (recipe_id shown instead of recipe details)

Issue: The profile page initially displayed raw `recipe_id` values instead of proper recipe cards.
Cause: The favourites table stores IDs only, while the template needed the meal name and thumbnail for display.
Fix: In the profile route, I looped through the saved IDs, looked each one up through TheMealDB, and passed full meal objects into `top3`.

---

### 8. CSS layout and hover consistency issues

Issue: Card layout and hover behavior were inconsistent across recipes, favourites, and profile.
Cause: Duplicate card classes and shared styling were pulling card and action behavior in different directions.
Fix: I standardized the card styling under `meal-card`, used clearer wrappers where needed, and added profile-specific responsive rules so the top cards stayed centered.

---

### 9. Code organisation

Issue: Early development placed most logic in one area, making growth harder to manage.
Cause: Features were added quickly before the structure was refined.
Fix: I reorganized `app.py` into clearer sections by responsibility so the code is easier to read and maintain.

---

### 10. Render cold start delays

Issue: The deployed app could be slow to respond after periods of inactivity due to Render spin-down.
Cause: On the free tier, inactive services may sleep and need extra startup time on the next request.
Fix: I configured cron-job.org to send a ping to GlobalGrub every 10 minutes to keep the service warm and reduce cold-start delays.

---

## Current limitations

The favourites system works, but the UI could still be improved further. Flash messages are not implemented yet. Recipe names from the API also vary in length, which can still affect layout consistency on the recipe and favourites pages.

---

## Future improvements

I plan to add a small JavaScript interactivity layer to improve usability without overcomplicating the application. The main addition will be a password visibility toggle on the login and signup forms, which will make it easier for users to enter credentials correctly. I also want to improve form validation feedback with simple regex-based checks for password strength, and optionally username formatting, so users get immediate visual feedback when inputs do not meet the required rules. In addition, I plan to replace blank error pages with clearer, user-friendly messages on the same page where the problem occurs. Overall, the aim is to keep JavaScript minimal and practical so that it supports the Flask backend rather than duplicating its responsibilities.

---

## What I learned

I learned how Flask applications are structured and how frontend and backend work together in a full-stack project. I also learned how authentication and sessions work, how SQLAlchemy queries such as `filter_by()` support user-specific data, how to handle API errors properly, and how system design changes as projects grow.

---

## Credits

**These sources were used as learning references and adapted to fit the specific requirements of this project.**

### Authentication system

Authentication system based on:

- [Python Flask Authentication Tutorial (GitHub)](https://github.com/neupanic/Python-Flask-Authentication-Tutorial)

As well as the YouTube video tutorial

**Used for:**
- Flask-Login setup  
- authentication flow  
- password hashing  

**Adapted for this project by:**
- connecting it to recipe system  
- adding favourites support  
- adjusting routing and templates  
- adding custom validation and error handling  

---

### Database and SQLAlchemy

Database setup and model structure were informed by:

- [Flask Mega-Tutorial Part IV: Database (Miguel Grinberg)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)

- [Connect Flask to a Database with Flask-SQLAlchemy (GeeksforGeeks)](https://www.geeksforgeeks.org/python/connect-flask-to-a-database-with-flask-sqlalchemy/)  

**Used for:**
- understanding how SQLAlchemy models are defined  
- structuring database tables using Python classes  
- basic database setup and configuration  
- learning how to create and initialise tables  

**Adapted for this project by:**
- creating a User model for authentication  
- creating a Favourite model to store saved recipes  
- linking favourites to users using a one-to-many relationship  
- integrating database logic into Flask routes  

---

### Flask Structure and Application Flow

General Flask structure and application flow were supported by:

- [Flask Tutorial (GeeksforGeeks)](https://www.geeksforgeeks.org/python/flask-tutorial/)  

**Used for:**
- understanding how Flask routes handle requests  
- how templates and backend logic connect  
- structuring the application from frontend to backend  
- reinforcing the request → route → response flow  

**Adapted for this project by:**
- organising routes for recipes, authentication, and favourites  
- using Jinja templates for dynamic page rendering  
- structuring query parameter handling for filtering  

---

### Favourites System Design (Derived Learning)

The favourites system design was built using combined understanding from:

- [Flask Mega-Tutorial Part IV: Database (Miguel Grinberg)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)  

- [Connect Flask to a Database with Flask-SQLAlchemy (GeeksforGeeks)](https://www.geeksforgeeks.org/python/connect-flask-to-a-database-with-flask-sqlalchemy/)  

**Applied in this project to:**
- separate favourites into their own table  
- avoid storing full recipe data locally  
- link users to saved recipes using foreign keys  
- query user-specific data securely using `filter_by()`  