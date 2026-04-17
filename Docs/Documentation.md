
# GlobalGrub Documentation

**Last updated:** April 17, 2026

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

At the start, API calls were handled using JavaScript `fetch()`.

This caused:
- messy frontend logic
- inconsistent data handling
- limited control over errors

Moving API logic to Flask fixed this by centralising everything in one place.

---

### 2. Understanding authentication

It took time to understand:
- how sessions work
- how `current_user` works
- why `user_loader` is needed

I learned that Flask-Login handles authentication by storing only the user ID in the session and rebuilding the user object on each request.

---

### 3. Route protection change (guest -> login_required)

At first, I planned to:
- allow guests to view the favourites page
- show a message asking them to log in

This was later changed to:
- `@login_required`

Reason:
- simpler logic
- better security
- cleaner route structure

---

### 4. Database issue

I encountered:
> no such table: user

This happened because the database tables were not created properly.

Fix:
```python
with app.app_context():
    db.create_all()
```

---

### 5. API reliability issues

The API sometimes returned:

* empty results
* missing fields
* inconsistent data

Fix:

* used `.get()` safely
* added fallback empty lists
* added error handling in routes

---

### 6. Favourites system and database relationships (major challenge)

One of the most challenging parts of the project was connecting users, saved recipes, and the external API data.

The main difficulty was understanding how to store favourites properly and how to link everything together.

At first, I considered storing favourites directly inside the User model, but this approach did not work well because:

* recipes come from an external API, not my database
* storing full recipe data would cause duplication and inconsistency
* it would be difficult to query saved recipes properly

To solve this, I created a separate Favourite table.

### Key challenges faced:

**Understanding relationships between tables**  
It took time to understand how a user can have many favourites and how each favourite links back to a single user.

---

**Favourites not appearing on favourites page**

At one stage, recipes could be successfully saved from the recipe page, and the UI (star icon) updated correctly, but nothing appeared on the favourites page.

This showed that:
- the frontend state was updating
- but the database query or route logic was not returning the saved data correctly

This required checking:
- whether favourites were actually being committed to the database
- whether the correct user ID was being used in the query
- whether the favourites route was properly filtering results using `current_user`

---

**Missing remove functionality**

Initially, only an "add favourite" route existed.

This caused a major issue:
- users could save recipes
- but could not remove them

Clicking the save button again did nothing because no remove logic existed.

To fix this, I added a separate remove route, which allowed:
- removing favourites from the recipe page
- removing favourites from the favourites page

This completed the full save/unsave functionality.

---

**Save/unsave logic**

Another challenge was handling how saving should behave when a recipe is already saved.

This required:
- checking if a favourite already exists in the database
- deciding whether to insert a new row or delete an existing one

Without this logic, the system would either:
- fail to remove items
- or behave inconsistently

---

**Querying user-specific data**

I used `query.filter_by()` to:

* get only the logged-in user’s favourites
* ensure users cannot see other users’ saved data

This was important because all users share the same favourites table.

---

**Connecting API data with database data**

A major challenge was that recipe data comes from TheMealDB API, while saved data is stored in SQLite.

This meant I had to match:

* API recipe IDs
* database stored `recipe_id` values

This required careful logic in routes and templates to:
- correctly display saved recipes
- show the correct saved/unsaved state (i.e. star icon)

---

**Multiple routes working together**

The favourites system required multiple routes working together:

- add favourite
- remove favourite
- favourites page

At first, not all of these were implemented, which caused incomplete functionality.

Once all routes were properly connected, the system worked as expected.

---

### 7. Code organisation

At the start, everything was inside one file:

* API logic
* authentication
* database queries
* route handling

Over time, I improved structure by grouping logic into clearer sections inside `app.py`.

---

## Current limitations

* Favourites system works but still needs UI improvements
* Flash messages are not implemented yet
* Profile page is basic and will be improved later
* Recipe names called from the API differ in length which causes inconsistent layout on recipe and favourites pages

---

## What I learned

* How Flask applications are structured
* How frontend and backend work together
* How authentication and sessions work
* How SQLAlchemy queries work (`filter_by`)
* How to handle API errors properly
* How system design changes as projects grow

---

## Credits

Authentication system based on:

[https://github.com/neupanic/Python-Flask-Authentication-Tutorial](https://github.com/neupanic/Python-Flask-Authentication-Tutorial)

As well as the YouTube video tutorial

Used for:

* Flask-Login setup
* authentication flow
* password hashing

Adapted for this project by:

* connecting it to recipe system
* adding favourites support
* adjusting routing and templates
* adding custom validation and error handling
