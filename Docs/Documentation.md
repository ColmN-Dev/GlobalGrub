# GlobalGrub Documentation

Last updated: April 12, 2026

## Overview

GlobalGrub is a Flask web application for exploring recipes from around the world using TheMealDB API. Users can browse recipes by country, search by meal name, and open a full recipe detail page.

---

## Current Architecture

The app uses a server-side Flask flow:

- Flask handles routing and data fetching
- TheMealDB provides recipe data
- Jinja templates render pages from route data
- JavaScript is used for small UI interactions only

---

## Current Routes

- `/` -> Home page with hero, marquee, and region cards
- `/countries` -> Lists all MealDB countries (A-Z)
- `/recipes` -> Search and region results page
- `/recipe/<id>` -> Single recipe details page
- `/about`, `/favourites`, `/auth/signup`, `/auth/login`, `/auth/profile` -> Template pages

---

## Recipes Route Behavior

The `/recipes` route supports three input values from query parameters:

- `search` -> meal name search
- `region` -> country/area filter
- `course` -> `all` or `dessert`

Current behavior:

- If `search` exists, data comes from `search.php?s=...`
- If `course=dessert` with search, results are narrowed to dessert category
- If `region` exists, data comes from `filter.php?a=...`
- If both search and region are empty, a user message is shown

---

## Countries Page

The `/countries` route calls `list.php?a=list`, extracts `strArea`, removes empty values, and sorts the list alphabetically before rendering.

Each country link points to:

- `/recipes?region=<country>`

This gives users a quick way to browse meals by region from one page.

---

## Recipe Detail Page

The `/recipe/<id>` route calls `lookup.php?i=<id>` and renders one meal.

It includes:

- meal title and metadata
- image
- instructions
- ingredient list

Ingredients are built by looping through TheMealDB fields `strIngredient1..20` and `strMeasure1..20`.

---

## Frontend and Styling Notes

- Shared layout is handled in `base.html`
- Main pages extend the base template
- UI is custom CSS with responsive breakpoints
- Navbar supports desktop links and a mobile slide-out menu
- Recipes page uses simple `All` / `Dessert` filter buttons

---

## Accessibility

- Added meaningful `alt` text for recipe and UI images
- Added `aria-label` to key search, filter, and menu controls
- Added `aria-expanded` and `aria-controls` to the mobile menu toggle
- Added a `title` attribute to the embedded recipe video iframe

---

## Tech Stack

- Python 3
- Flask
- Requests
- Jinja templates
- HTML/CSS/JavaScript
- Gunicorn (deployment)
- Render (hosting)

---

## Known Gaps / Next Steps

These are planned but not fully implemented in the current app state:

- complete auth/session flow (including logout handling)
- persistent favourites storage
- persistent user profile data
