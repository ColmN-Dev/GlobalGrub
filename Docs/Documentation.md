# GlobalGrub Documentation

## Overview

**GlobalGrub** is a Flask web application I built to let users browse and discover recipes from around the world using TheMealDB API. Users can explore meals by region, search for recipes using keywords, and view detailed recipe pages.

I used **Flask (Python)** for the backend, **Jinja templates** for rendering dynamic pages, and minimal JavaScript mainly for small UI interactions.

---

## Design Decisions and Theme

- I chose a warm, evening restaurant-style theme because I wanted the site to feel more like a food experience rather than just a recipe database.
- I used **Cinzel** for headings to give the site a more styled, branded look, and **Times New Roman** for body text because it is simple and readable.
- I kept the structure focused on how users naturally navigate:
  - Browse by region
  - Search for recipes
  - View recipe details

- The homepage uses a grid-based region selector, where each card links to filtered recipe pages using Flask URL parameters.

- Each region uses **unique images per country**, improving visual clarity and ensuring accurate representation of each cuisine category.

---

## Core Application Architecture

GlobalGrub is built using a **server-side Flask architecture**, where the backend controls all application logic.

- Flask handles all routing and page rendering.
- URL parameters (`request.args`) control filtering (search and region).
- TheMealDB API is used as the external data source.
- Jinja templates render dynamic content based on data passed from Flask.

This ensures that Flask acts as the single source of truth for application behaviour, with the frontend focused only on display.

---

## Flask Role in the Application

Flask is responsible for:

- Routing between pages (home, recipes, recipe detail, etc.)
- Handling user input through URL parameters
- Fetching data from TheMealDB API
- Processing and filtering responses
- Passing data into Jinja templates for rendering

I kept most logic in Flask to maintain consistency and avoid splitting behaviour across frontend and backend.

---

## Development Process

- I started by setting up Flask with multiple routes and basic templates.
- I used template inheritance to avoid repeating layout elements like the navbar and footer.
- I implemented region-based browsing using URL query parameters.
- I added search functionality through Flask by calling TheMealDB API directly.
- I improved the UI using grid layouts, hover effects, overlays, and responsive design.
- Over time, I simplified the backend so Flask became the central controller for all data and filtering logic.

---

## Challenges Faced

The main challenges I faced were integrating backend and frontend features into a single consistent system.

On the **backend (Flask / Python)** side, the biggest difficulty was handling multiple user states within the `/recipes` route. I needed to support region filtering, valid searches, and empty search submissions all within the same endpoint. Initially, I had issues with incorrect condition ordering and misunderstanding how Flask handles request parameters, which caused inconsistent messages and behaviour. I resolved this by simplifying the logic and ensuring Flask handled all decision-making.

On the **frontend (Jinja, JavaScript, CSS)** side, I had to ensure the templates only displayed data coming from Flask without duplicating logic. This was important for keeping behaviour consistent and avoiding conflicting states between backend and frontend.

I only used **JavaScript** for small UI interactions such as clearing the search input and handling basic form behaviour. The challenge here was making sure these interactions did not interfere with Flask-based routing or page reloads.

For **CSS**, the main issues were layout and responsiveness. I had problems with inconsistent grid behaviour when displaying different numbers of results, as well as image scaling across devices. I resolved this using consistent grid structures, fixed card sizing, and `object-fit: cover`. I also refined media queries to ensure the layout adapted properly across mobile and desktop screens.

Overall, the biggest challenge was getting Flask, Jinja, JavaScript, and CSS to work together cleanly without overlapping responsibilities. Once I moved all logic into Flask and simplified frontend behaviour, the application became much more stable and predictable.

---

## Python / Flask Components

Flask manages all application routes and API communication.

### Routes:
- `/` → Home page  
- `/recipes` → Search and region filtering  
- `/recipe/<id>` → Individual recipe page  
- `/about`, `/favourites`, `/auth/*` → Static pages  

---

## Recipe Data Flow

User interactions are controlled through URL parameters:

- Region selection:
```

/recipes?region=Irish

```

- Search:
```

/recipes?search=chicken

```

Flask processes these parameters, calls TheMealDB API, and renders results dynamically using Jinja templates.

---

## JavaScript Components

JavaScript is used minimally for UI enhancements:

- Mobile navigation toggle
- Clearing search input
- Basic form interactions

All core data handling is managed by Flask.

---

## Recipe Detail Page

Each recipe is accessed using:

```

/recipe/<id>

```

This page displays:

- Meal image
- Title and category
- Ingredients and measurements
- Cooking instructions
- Embedded YouTube video (if available)

All elements are styled using css classes for cross-page consistency 

Ingredients are extracted in Python by looping through API fields (`strIngredient1–20`).

---

## Region System

### Americas
- American
- Canadian
- Mexican
- Argentinian

### Europe
- Italian
- Spanish
- Irish
- Polish

### Asia
- Chinese
- Indian
- Japanese
- Thai

### Global
- All Recipes (no filter)

---

## Frontend Features

- Marquee image strip built using CSS animations for continuous scrolling effect
- Region cards using grid layout with hover scaling and overlay text
- Hero section with themed food imagery and visual emphasis
- Fully responsive design using media queries
- Meal cards with fixed sizing and consistent image cropping

---

## Future Improvements

- User authentication system with secure password hashing
- Favourites system using database storage (SQLite / SQLAlchemy)
- Improved empty-state and loading UI feedback
- Deployment using environment variables on a hosting platform
- User profile system and personalization features
