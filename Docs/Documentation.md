# GlobalGrub Documentation

## Overview

**GlobalGrub** is a Flask web application I built that allows users to browse recipes from around the world, discover dishes by region, and search meals using TheMealDB API. The project combines Flask backend routing with frontend interactivity using HTML, CSS, and vanilla JavaScript.

---

## Design Decisions and Theme

- I chose a single warm evening restaurant aesthetic instead of multiple themes. I originally considered a darker forest-style background, but I removed it because it didn’t fit the food focus and hurt readability.

- I used **Cinzel** for headings and branding and **Times New Roman** for body text to keep things readable. I kept italic styling across key UI elements for consistency.

- I built responsiveness gradually instead of at the end, which made it easier to fix layout issues as they appeared across desktop and mobile.

- The navbar is fixed with a mobile hamburger menu. The hero section is the main visual focus with a hover saturation effect. I used `pointer-events: none` on overlay text so it doesn’t block clicks.

- I used a full background image with semi-transparent overlays to keep text readable.

- I built a marquee using CSS animation with duplicated images for a seamless loop. It pauses on hover and increases saturation.

- I built a region selector using a CSS grid. Each card links to filtered recipes using query parameters like `/recipes?region=asian`. Labels are absolutely positioned with `pointer-events: none`.

---

## Development Process

1. I set up Flask and created routes for all main pages.

2. I used Flask template inheritance so I didn’t have to repeat the navbar and footer.

3. I built the frontend step by step, starting with layout, then adding hero, marquee, and region cards.

4. I added TheMealDB API search using fetch and rendered results dynamically as cards.

5. I improved responsiveness as I went by adjusting layout and sizing for different screens.

---

## Challenges Faced

- The fixed navbar was covering content, so I fixed it by adding top padding to the body.

- The marquee didn’t loop smoothly at first, so I duplicated the images and used a `translateX(-50%)` animation.

- Recipe cards were aligning to the left on some layouts, so I fixed it by adjusting flex/grid centering.

- Images were inconsistent in size, so I standardised `object-fit` and height rules.

- I had mobile overflow issues causing horizontal scrolling, which I fixed using layout constraints and `overflow-x: hidden`.

- Region labels needed to stay centered without blocking hover effects, so I used absolute positioning and `pointer-events: none`.

- I originally used a `ul` list for ingredients, but I changed it to a table to make the ingredient names and measurements easier to read.

- Search UI state (input, results, clear button) was inconsistent, so I refactored it to keep everything in sync.

---

## JavaScript Components

- I implemented a hamburger menu for mobile navigation using class toggles.

- I built a recipe search system using TheMealDB API with fetch, rendering up to 12 results dynamically.

- I added clear search functionality and Escape key support to reset the UI.

---

## Python/Flask Components

- I created Flask routes for all pages including home, recipes, login, signup, profile, favourites, and about.

- I used template inheritance to avoid repeating layout code.

- I passed region filters through URL query parameters using `url_for()`.

---

## Recipe Detail Page

Each recipe has its own dedicated page that is accessed only by clicking a search result. It is not directly available through the navbar.

The page displays:
- Meal image
- Title
- Region/category
- Embedded YouTube video (if available)
- Ingredients shown in a table format
- Cooking instructions

Originally, I used an unordered list for ingredients, but I changed it to a table to make the layout clearer and easier to scan.

---

## Future Enhancements

- Add full user authentication with password hashing and sessions.

- Add user profiles with avatars and preferences.

- Build favourites system using SQLite and SQLAlchemy.

- Add filtering, sorting, and pagination for recipes.

- Deploy to Render with environment variables.