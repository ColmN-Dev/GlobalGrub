# GlobalGrub Documentation

## Overview

**GlobalGrub** is a Flask web application that allows users to browse recipes from around the world, discover dishes by region, and view a curated home page with interactive elements. The project focuses on backend integration with Flask and frontend interactivity using custom HTML, CSS, and JavaScript.

---

## Design Decisions and Theme

- **Single Theme Approach**: Initially, I considered implementing a full dark mode with a nighttime forest background. After evaluating the complexity and impact on readability, I decided to stick with a single "mixed" theme. The forest background was later replaced with an evening outdoor restaurant scene featuring a warm sunset vibe. This new background better fits the food and dining theme of the site while maintaining the warm, inviting atmosphere.

- **Font Choices**: The app primarily uses **Cinzel** for headings and the brand, giving a classic, elegant feel, and **Times New Roman** for paragraph text to complement readability and traditional aesthetic. I also use `font-style: italic` throughout for stylistic consistency.

- **Responsive Design**: I wanted to build responsive features progressively as I went along, rather than after completing the layout. This allowed me to adjust font sizes, navbar layout, hero section dimensions, and region card layouts incrementally, making the interface usable across both desktop and mobile devices without major rework.

- **Navbar and Hero**: The navbar is fixed at the top for quick access and includes a hamburger menu for mobile devices. The hero section uses a globe with plate, knife, and fork as the main visual, with subtle hover effects (`:hover { filter: saturate(1.5); }`) to add interactivity without distracting from content. The hero text has `pointer-events: none` so clicks pass through to the image underneath.

- **Background and Imagery**: An evening outdoor restaurant background with warm sunset tones sets the mood, with overlay boxes and semi-transparent containers providing readability. Images are scaled and optimized to avoid layout issues on smaller screens. Hover effects on images increase saturation (`filter: saturate(1.5)`) and scale (`transform: scale(1.2)`) to create engaging visual feedback.

- **Marquee Strip**: Below the hero section there is a continuously scrolling marquee of food images built entirely with CSS animations. The marquee uses `translateX(-50%)` with duplicated image sets to create a seamless infinite loop with no snapping. The images are styled as fixed-size squares (200x200px on desktop, 150x150px on mobile) with `object-fit: cover` to keep them consistent regardless of the original image dimensions. The marquee container has a dark semi-transparent background (`rgba(0,0,0,0.7)`) to contrast against the restaurant page background and make the images pop. **Pause on Hover**: The marquee pauses when the user hovers over it (`:hover { animation-play-state: paused; }`), allowing users to examine individual dishes more closely while also applying a saturation boost for visual emphasis.

- **Region Selector**: Below the marquee, four region cards (Asian, European, American, All Regions) are displayed in a responsive CSS grid. Each card shows a food image representative of that region with an overlaid region name centered at the bottom. The region names use `position: absolute` with `pointer-events: none` so hover effects on the images work seamlessly even when hovering over the text. Each card links to the Recipes page with a query parameter (e.g., `/recipes?region=asian`) to filter recipes by the selected region. Cards have hover effects that scale the image and increase saturation for visual feedback.

---

## Development Process

1. **Backend Setup**: Flask installed and base routes configured for all pages.
2. **Frontend**:
   - Base template with navbar and footer implemented.
   - Custom CSS for styling and hero section added.
   - Mobile styles included via media queries.
   - Responsive design handled incrementally during development.
   - Marquee strip added below the hero section using CSS `@keyframes` animation with pause-on-hover functionality.
   - Region selector cards implemented with CSS Grid layout, overlay text labels, and query parameter links to Recipes page.
   - Hover effects (saturation boost and scale transform) applied to hero image, marquee images, and region cards.
   - Background changed from forest theme to evening outdoor restaurant scene for better thematic fit.
3. **JavaScript**:
   - Hamburger menu toggle implemented (`.hamburger` and `.mobile-menu` classes) in `main.js`.
   - JavaScript files organized by page/feature (e.g., `main.js` for global functionality, page-specific files for other features).

---

## Challenges Faced

- Adjusting the navbar and hero text to work properly across different screen sizes.
- Ensuring the fixed navbar did not overlap page content.
- Working out responsive layout for mobile without breaking desktop view.
- Getting the marquee to loop seamlessly without snapping and fixing the left-gap issue caused by nesting it inside the `hero-container`.
- Positioning region name overlays on cards so they remain visible and centered across different screen sizes while allowing hover effects to work when hovering over the text (`pointer-events: none` solution).
- Ensuring the region name background boxes fit the text content tightly using `width: fit-content` instead of stretching full width.

---

## JavaScript Components

- **Hamburger Menu**: Slide-out menu toggle on mobile devices using `.mobile-menu.open` class and body scroll lock (`body.menu-open`). Located in `main.js` as it's used across all pages.

---

## Python/Flask Components

- **Routes**: Base routes implemented for each page (home, recipes, login, signup, profile, favourites, about).
- **Template Rendering**: Flask's templating system used to avoid repeating navbar/footer (`{% extends "base.html" %}`).
- **Query Parameters**: Region links use Flask's `url_for()` with query parameters (`{{ url_for('recipes', region='asian') }}`) to pass the selected region to the Recipes page.

---

## Future Enhancements

- **Recipes Page**: Hardcoded carousel of featured recipes, TheMealDB API search bar, region filtering based on URL query parameters, carousel/tabs to switch between regions.
- **Login/Signup System**: User authentication with password hashing and Flask sessions.
- **User Profiles**: Custom avatar picker modal (PlayStation-style grid), display user info and stats.
- **Favourite Recipes**: Save and manage favourite recipes with database storage, guest lockout on Favourites page.
- **Database**: SQLite with Flask-SQLAlchemy for Users and Favourites tables.
- **Deployment**: Deploy to Render.com.