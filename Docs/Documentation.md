# GlobalGrub Documentation

**Last updated:** April 25, 2026

---

## Overview

GlobalGrub is a Flask web application built for browsing recipes from around the world using TheMealDB API. The project started as a mainly frontend-focused build with some early backend ideas, and later developed into a full-stack application with Flask routes, database storage, user authentication, and a favourites system. The main development focus moved step-by-step from UI design to API integration, then to backend structure, and finally to user accounts and saved data.

---

## Project Development

### 1. Initial frontend-focused version (with early backend ideas)
The project started mainly on the frontend side using HTML, CSS, and JavaScript. At this stage, the focus was on page layout and design, the recipe card UI, navigation between pages, and the basic structure for future backend features. There was already an idea of using Flask later, but most of the early work was focused on the frontend experience.

---

### 2. Using JavaScript fetch for API
I originally used `fetch()` in JavaScript to get data from TheMealDB API. This worked because I was familiar with JavaScript from a previous project, it was quick to set up, and it allowed recipes to load directly in the browser. However, issues appeared as the project grew because the frontend logic became messy, API handling was spread across files, error handling was limited, and it was difficult to manage data across multiple pages.

---

### 3. Moving API logic to Flask backend
I moved API requests into Flask routes to improve the project. This change centralised the API logic in the backend, simplified the frontend JavaScript, made data handling more consistent, and allowed for the use of Jinja templates for rendering pages. At this point, the project became a full Flask web application.

---

### 4. Search and filtering system
I added a search by meal name, a filter by region or country, and a filter by course type for all or desserts. This was handled using query parameters in Flask, specifically `search`, `region`, and `course`. Using query parameters kept the routing flexible and simple.

---

### 5. Error handling improvements
After building the main routes, I added error handling. This included `try/except` blocks around API calls, timeout handling set to 10 seconds, and safe fallback values when the API returns empty data. This was needed because the API sometimes returns empty results, is slow to respond, or returns missing fields.

---

### 6. Authentication system
Later in the project, I added user accounts using Flask-Login, Flask-Bcrypt, and an SQLite database with SQLAlchemy. This allowed for user registration, login/logout, session-based authentication, and secure password storage through hashing. I learned that Flask-Login stores only the user ID in the session and reloads the full user from the database on each request.

---

### 7. Profile route and profile page
I added a dedicated profile route and connected it to a new profile UI. The backend additions included counting total saved favourites for the logged-in user, selecting the latest saved favourites, and fetching full meal details from TheMealDB for display. The frontend additions included a profile header with user information, a total saved recipes summary, the top 3 recent favourite recipe cards, and quick actions like viewing all favourites and logging out. This was important because favourites in the database only store recipe IDs, so the profile page needed extra route logic to transform IDs into full recipe data before rendering.

---

### 8. JavaScript Interactivity
I implemented a JavaScript layer to improve usability without overcomplicating the application. The features added included a mobile hamburger menu toggle that auto-closes on navigation, and a search input clear button that also responds to the Escape key. The main addition was a password visibility toggle on the login and signup forms, which switches the input between `password` and `text` to help users enter credentials correctly. A loading spinner was also added to the recipes page search form, which appears and dims the previous results while a new search request is loading. JavaScript is also used to dynamically update ARIA attributes at runtime, such as `aria-expanded` on the hamburger menu, `aria-busy` on the results area during loading, and `aria-pressed` and `aria-label` on the password toggle. This ensures JavaScript remains minimal and practical, supporting the Flask backend rather than duplicating its responsibilities.

---

## Design Decisions

### Theme choice
I originally planned a forest-style theme with a day/night toggle but changed this because it added unnecessary complexity and made styling harder to keep consistent. I instead chose a warm restaurant or evening dining style with soft dark UI elements to focus on food presentation.

---

### UI design choices
To improve usability, I added hover effects on cards and buttons, smooth CSS transitions, and consistent spacing and layout rules. These were added gradually during development to ensure a polished feel.

---

### Backend choices
I chose Flask for backend logic and routing, while SQLite was used for simple local database storage. Jinja templates were used instead of frontend frameworks, and I chose Flask-Login for authentication instead of a custom login system. These choices were made to keep the project simple and manageable.

---

### Routing approach
Instead of creating many separate pages, I used one main route at `/recipes`. Filtering is handled using query parameters, which made the system easier to manage, more flexible, and easier to extend later.

---

### "Are you sure?" removal modal
I decided to keep the removal process direct rather than adding a confirmation modal. A quick, single-click removal keeps the experience fast and reduces unnecessary steps for the user.

---

### Database design (`query.filter_by`)
I used `query.filter_by()` in SQLAlchemy to retrieve specific data from the database, such as finding favourites for a specific user or checking if a recipe is already saved. This is useful because it allows filtering by column values easily, keeps the code readable, and avoids writing raw SQL. This was important for the favourites system because each user must only see their own saved recipes.

---

## Problems and Challenges

### 1. Frontend -> backend migration
The issue was that API calls were spread across frontend JavaScript and became hard to maintain. This happened because as the app grew, search, filtering, and error handling were split across multiple files. To fix this, I moved API logic into Flask routes and rendered the data through Jinja templates so the flow stayed in one place.

---

### 2. JavaScript Selection and Logic
I encountered issues where interactive elements were not responding correctly. The cause was incorrectly using `querySelectorAll` for single elements and running scripts on pages where elements did not exist. I corrected the selectors to `getElementById` and added checks to ensure scripts only run when specific elements are present.

---

### 3. Understanding authentication
The authentication flow was unclear at first. This was because I needed to understand sessions, `current_user`, `user_loader`, and how Flask-Login rebuilds the user on each request. I fixed this by mapping the full login lifecycle and aligning the routes with the Flask-Login session model.

---

### 4. Route protection change (guest -> login_required)
The first idea was to let guests open the favourites page and show a login message. However, the mixed guest and authenticated behavior made the route logic more complicated than it needed to be. I switched to `@login_required`, which kept the route cleaner and ensured only logged-in users could access saved data.

---

### 5. Database issue
I hit a `no such table: user` error during authentication testing. This was caused by the database tables not being initialized in the active app context, so the models existed in code but not in SQLite. I fixed this by ensuring `db.create_all()` runs inside `app.app_context()` so the tables are created when the app starts.

---

### 6. API reliability issues
TheMealDB responses were sometimes empty, partial, or inconsistent. This was due to external API reliability varying across endpoints and missing fields. I fixed this by using safe `.get()` lookups, fallback defaults, and route-level error handling to keep the pages from breaking.

---

### 7. Favourites system and database relationships
Linking users, favourites, and API recipes was the most complex part of the project. Because recipe data comes from the API but the app only stores `recipe_id` locally, the database and API had to be coordinated carefully. I created a separate `Favourite` model, added add/remove routes, and used user-scoped `filter_by()` checks so each user only sees their own saved recipes.

---

### 8. Profile data mismatch
The profile page initially displayed raw `recipe_id` values instead of proper recipe cards. This happened because the favourites table stores IDs only, while the template needed the meal name and thumbnail. In the profile route, I looped through the saved IDs, looked each one up through TheMealDB, and passed the full meal objects into the template.

---

### 9. CSS layout and hover consistency issues
Card layout and hover behavior were inconsistent across recipes, favourites, and profile pages. This was caused by duplicate card classes pulling styling in different directions. I standardized the card styling under `meal-card`, used clearer wrappers, and added profile-specific rules so the cards stayed centered.

---

### 10. Render cold start delays
The deployed app was slow to respond after inactivity due to Render's spin-down behavior on the free tier. To fix this, I configured **cron-job.org** to send a ping to GlobalGrub every 10 minutes to keep the service warm and reduce cold-start delays.

---

## Current limitations

The favourites system works, but the UI could still be improved further. Flash messages are not implemented yet. Recipe names from the API also vary in length, which can still affect layout consistency on the recipe and favourites pages. There is no frontend form validation currently implemented.

---

## Future improvements

I plan to add stronger form validation feedback with simple regex-based checks for password strength so users get immediate visual feedback. In addition, I plan to replace blank error pages with clearer, user-friendly messages on the same page where the problem occurs. Overall, the aim is to keep JavaScript minimal and practical so that it supports the Flask backend.

---

## What I learned

I learned how Flask applications are structured and how frontend and backend work together in a full-stack project. I also learned how authentication and sessions work, how SQLAlchemy queries such as `filter_by()` support user-specific data, how to handle API errors properly, and how system design changes as projects grow.

---

## Credits

**These sources were used as learning references and adapted to fit the specific requirements of this project.**

### Authentication system
Authentication system based on the [Python Flask Authentication Tutorial (GitHub)](https://github.com/neupanic/Python-Flask-Authentication-Tutorial) as well as associated YouTube video tutorials.
**Used for:** Flask-Login setup, authentication flow, and password hashing.
**Adapted for this project by:** Connecting it to the recipe system, adding favourites support, adjusting routing and templates, and adding custom validation and error handling.

---

### Database and SQLAlchemy
Database setup and model structure were informed by:
- [Flask Mega-Tutorial Part IV: Database (Miguel Grinberg)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
- [Connect Flask to a Database with Flask-SQLAlchemy (GeeksforGeeks)](https://www.geeksforgeeks.org/python/connect-flask-to-a-database-with-flask-sqlalchemy/)
**Used for:** Understanding how SQLAlchemy models are defined, structuring database tables using Python classes, basic database setup, and learning how to create and initialise tables.
**Adapted for this project by:** Creating a User model for authentication, creating a Favourite model to store saved recipes, linking favourites to users using a one-to-many relationship, and integrating database logic into Flask routes.

---

### Flask Structure and Application Flow
General Flask structure and application flow were supported by:
- [Flask Tutorial (GeeksforGeeks)](https://www.geeksforgeeks.org/python/flask-tutorial/)
**Used for:** Understanding how Flask routes handle requests, how templates and backend logic connect, structuring the application from frontend to backend, and reinforcing the request-route-response flow.
**Adapted for this project by:** Organising routes for recipes, authentication, and favourites, using Jinja templates for dynamic page rendering, and structuring query parameter handling for filtering.

---

### Favourites System Design (Derived Learning)
The favourites system design was built using combined understanding from the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database) and [GeeksforGeeks SQLAlchemy resources](https://www.geeksforgeeks.org/python/connect-flask-to-a-database-with-flask-sqlalchemy/).
**Applied in this project to:** Separate favourites into their own table, avoid storing full recipe data locally, link users to saved recipes using foreign keys, and query user-specific data securely using `filter_by()`.

---

### JavaScript Interactivity
The logic for password visibility was supported by:
- [Show/Hide Password Using JavaScript (GeeksforGeeks)](https://www.geeksforgeeks.org/javascript/show-hide-password-using-javascript/)
**Used for:** Implementing the password visibility toggle functionality on login and signup forms to improve user credential entry.