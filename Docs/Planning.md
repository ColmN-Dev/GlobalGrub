# GlobalGrub — Project Plan

## What is GlobalGrub?

GlobalGrub is a Flask web app I'm building for my Python assignment. The goal is to let users discover recipes from different cuisines and save their favourites. I'll be using Flask (Python) for the backend, HTML/CSS for the frontend, and JavaScript for interactivity. The app will be deployed using Render.

---

## Pages

The app will use multiple HTML templates inside a `templates` folder. I'll have a `base.html` file that contains the navbar and footer so I don't have to repeat that on every page. Other pages will extend this.

Pages I plan to include:
- Home (`home.html`)
- Recipes (`recipes.html`)
- Favourites (`favourites.html`)
- Profile (`profile.html`)
- About (`about.html`)
- Login and Sign Up (`auth/login.html`, `auth/signup.html`)

---

## Project Structure

- `app.py`  
- `globalgrub.db`  
- `requirements.txt`  
- `render.yaml`  
- `templates/` (with an `auth/` folder inside it)  
- `static/` (`css/`, `js/`, `images/`)  
- `docs/`  

---

## Core Functionality

- Users can sign up and log in using Flask sessions  
- Users can search for recipes using TheMealDB API  
- Recipes will be displayed as cards  
- Logged in users can save recipes  
- The UI will change depending on whether the user is logged in or not  

---

## Database

I'll be using SQLite with Flask-SQLAlchemy.

There will be two tables:
- **Users** → id, username, password (hashed), avatar  
- **Favourites** → saved recipes linked to a user  

This will let each user have their own saved recipes.

---

## Authentication System

Users will be able to register and log in. Their details will be stored securely in the database.

Flask sessions will keep track of whether a user is logged in, and the navbar will change depending on that. I'll also add basic form validation like checking for empty fields and making sure usernames are unique.

---

## Application Flow

1. User signs up or logs in  
2. User searches for a recipe  
3. Flask sends a request to the API  
4. Results are shown as recipe cards  
5. User can save a recipe  
6. Saved recipes appear in the Favourites page  

---

## Frontend Design

The app will follow a forest-style theme.

I originally plan to include both light mode and dark mode, so the layout and colours will be designed with that in mind.

The site will be responsive so it works on mobile and desktop.

Main UI parts:
- Fixed navbar  
- Hero section  
- Recipe cards  
- Carousel section  

JavaScript will handle things such as:
- Carousel filtering  
- Mobile hamburger menu  
- Dark mode toggle  
- Small UI updates  

---

## Flask Implementation

All the backend logic will be in `app.py`.

- Each page will have its own route  
- Forms (like login and signup) will use POST requests  
- I'll use the `requests` library to get data from the API  
- Templates will be rendered using Jinja  

---

## Deployment

The app will be deployed on Render and connected to my GitHub repository. It will be run using Gunicorn.

---

## Further Goals

- User avatars  
- Better filtering options  
- Improved UI styling  
- Handling API errors properly  

---

## Wireframes

### Home Page Wireframe 
![Home Page Wireframe](../static/images/wireframes/Home_page.png)

This shows the layout of the home page with the navbar, hero section, and main content areas. I planned this with both light and dark mode in mind.

---

### Recipes Page Wireframe 
![Recipes Page Wireframe](../static/images/wireframes/Recipes_page.png)

This focuses on the recipes page, including the search bar, results, and carousel. It helped me plan how users will browse recipes.

---

### Profile Page Wireframe
![Profile Page Wireframe](../static/images/wireframes/Profile_page.png)

This shows the profile layout with user info and account features. It was used to plan how user data will be displayed.