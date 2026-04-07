# GlobalGrub Documentation

## Overview

**GlobalGrub** is a Flask web application that allows users to browse recipes from around the world and view a simple home page with a hero section. The project focuses on backend integration with Flask and frontend interactivity using custom HTML, CSS, and JavaScript.

---

## Design Decisions and Theme

- **Single Theme Approach**: Initially, I considered implementing a full dark mode with a nighttime forest background. After evaluating the complexity and impact on readability, I decided to stick with a single “mixed” theme. This theme combines darker UI elements like the navbar and overlay boxes with lighter content areas and text, ensuring good contrast and a consistent user experience across the app.

- **Font Choices**: The app primarily uses **Cinzel** for headings and the brand, giving a classic, elegant feel, and **Times New Roman** for paragraph text to complement readability and traditional aesthetic. I also use `font-style: italic`.

- **Responsive Design**: I wanted to build responsive features progressively as I went along, rather than after completing the layout. This allowed me to adjust font sizes, navbar layout, and hero section dimensions incrementally, making the interface usable across both desktop and mobile devices without major rework.

- **Navbar and Hero**: The navbar is fixed at the top for quick access and includes a hamburger menu for mobile devices. The hero section uses a globe with plate, knife, and fork as the main visual, with subtle hover effects (`:hover`) to add interactivity without distracting from content. Hover effects were carefully implemented on the hero section and cards to improve user engagement.

- **Background and Imagery**: A forest-themed background sets the mood, with overlay boxes and semi-transparent containers providing readability. Images are scaled and optimized to avoid layout issues on smaller screens.

---

## Development Process

1. **Backend Setup**: Flask installed and base routes configured.  
2. **Frontend**:  
   - Base template with navbar and footer implemented.  
   - Custom CSS for styling and hero section added.  
   - Mobile styles included via media queries.  
   - Responsive design handled incrementally during development.  
3. **JavaScript**:  
   - Hamburger menu toggle implemented (`.hamburger` and `.mobile-menu` classes).  

---

## Challenges Faced

- Adjusting the navbar and hero text to work properly across different screen sizes.  
- Ensuring the fixed navbar did not overlap page content.  
- Working out responsive layout for mobile without breaking desktop view.  

---

## JavaScript Components

- **Hamburger Menu**: Slide-out menu toggle on mobile devices using `.mobile-menu.open` class.  

---

## Python/Flask Components

- **Routes**: Base routes implemented for each page.  
- **Template Rendering**: Jinja2 templates used to avoid repeating navbar/footer (`{% extends "base.html" %}`).  

---

## Future Enhancements

- Login/signup system.  
- User profiles and favourite recipes.  
- API integration for recipe search.  
- Dark mode toggle.  
- Avatar picker modal.