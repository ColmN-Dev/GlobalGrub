# GlobalGrub Documentation

## Overview

**GlobalGrub** is a Flask web application I built to let users browse and discover recipes from around the world using TheMealDB API. Users can explore meals by region, search recipes using keywords, and view detailed recipe pages. The app uses Flask for backend routing, Jinja templates for rendering, and minimal JavaScript for UI interactions.

---

## Design Decisions and Theme

- I chose a warm, evening restaurant-style aesthetic to keep the UI food-focused and visually inviting. The background changed from a forest theme early on to an outdoor restaurant scene with sunset tones, which better fit the food and dining concept.

- Typography uses **Cinzel** for branding and headings to give an elegant feel, with **Times New Roman** for body text to maintain readability and a traditional aesthetic.

- The UI is structured around simplicity and discovery: region browsing → search → recipe details.

- The homepage uses a grid-based region selector. Each card links to filtered recipes using URL query parameters like `/recipes?region=Italian`.

- A single **"All Recipes"** option allows users to browse everything without filtering.

- Images are grouped by region type and reused consistently across multiple countries for simplicity.

---

## Core Application Flow

I built the app using a **server-driven filtering model** (no frontend fetch for search/results).

1. User clicks a region or submits a search
2. Flask reads URL parameters (`request.args`)
3. Flask calls TheMealDB API
4. Results are passed into Jinja templates
5. HTML renders meal cards dynamically

---

## Development Process

1. I initialized the Flask project with multiple routes (home, recipes, recipe detail, auth pages).

2. I used template inheritance to avoid repeating layout components (navbar, footer).

3. I implemented region-based browsing using URL query parameters.

4. I migrated the search system from JavaScript fetch to Flask-controlled API calls for cleaner architecture.

5. I improved the UI using grid layouts, overlays, hover effects, and responsive design.

---

## Challenges Faced

- Fixed navbar overlapping content was resolved using proper padding on the body.

- Marquee animation required duplicated elements for smooth looping without snapping.

- Image inconsistencies were fixed using `object-fit: cover`.

- Mobile responsiveness issues were resolved with grid adjustments and media queries per breakpoint.

- Region labels were refined using absolute positioning, overlays, and `pointer-events: none` so hover effects work properly.

- Search UI state issues were handled with minimal JavaScript for input validation.

- I removed fetch-based frontend search to avoid duplication with Flask logic and keep everything server-side.

- Getting meal card images to display properly side-by-side without stretching took adjusting the grid and switching to flexbox with fixed widths.

---

## Python / Flask Components

Flask handles all routing and API communication.

### Routes:
- `/` → Home page  
- `/recipes` → Search + region filtering  
- `/recipe/<id>` → Recipe detail page  
- `/about`, `/favourites`, `/auth/*` → Static pages  

---

## Recipe Filtering Logic

The `/recipes` route uses URL parameters:

### Region filter
```
/recipes?region=Italian
```

Uses:
```python
https://www.themealdb.com/api/json/v1/1/filter.php?a=Italian
```

---

### Search filter
```
/recipes?search=chicken
```

Uses:
```python
https://www.themealdb.com/api/json/v1/1/search.php?s=chicken
```

---

### Default state
No auto-loaded results (empty state or optional browse mode)

---

## JavaScript Components (Minimal Role)

I kept JavaScript minimal and only used it for UI interactions:

- Mobile hamburger menu toggle in `main.js`
- Search input clear button
- Input validation (prevent empty submissions)

Search is now fully handled by Flask (no fetch API).

---

## Recipe Detail Page

Each recipe is accessed via:
```
/recipe/<id>
```

Displays:
- Meal image
- Title
- Category/region
- Embedded YouTube video (if available)
- Ingredients and measurements (generated in Python)
- Cooking instructions

Ingredients are extracted from API fields `strIngredient1–20`.

---

## Region System

### Americas
- American
- Mexican

### Europe
- Italian
- French
- Greek
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

All regions use:
```python
url_for('recipes', region='X')
```

---

## Frontend Features

- **Marquee strip**: Continuously scrolling food images built with CSS `@keyframes` animation. Pauses on hover using `animation-play-state: paused` and applies a saturation boost for visual emphasis.

- **Region cards**: Grid layout with overlay text labels using `position: absolute` and `pointer-events: none`. Hover effects scale images and increase saturation.

- **Hero section**: Globe and fork banner image with overlay text. Hover applies saturation filter.

- **Responsive design**: Built progressively with media queries. Navbar collapses to hamburger menu on mobile, hero and marquee images scale down, region cards adjust height.

- **Meal cards**: Flexbox layout with fixed 220px width, 200px image height using `object-fit: cover`. Hover effects lift cards and add shadow.

---

## Future Improvements

- Authentication system (hashed passwords + sessions)
- Favourites system with SQLite + SQLAlchemy
- Pagination for large result sets
- Improved search UX (server-side enhancements)
- Deployment to Render with environment variables
- Better loading and empty-state UI handling
- Profile page with PlayStation-style avatar picker modal
