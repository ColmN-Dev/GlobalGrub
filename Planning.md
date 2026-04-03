# GlobalGrub — Project Plan

## What is GlobalGrub?

GlobalGrub is a Flask web application I am building for my Python assignment. The idea behind it is to create a place where users can discover recipes and dishes from different cuisines around the world. I came up with the name because it reflects the global nature of the app and feels catchy and memorable. The app will be built using `Flask` and `Python` on the backend, custom `CSS` for all the styling, and `JavaScript` for the interactive parts. The finished app will be hosted on `Render.com` and connected to a `GitHub` repository.

## Pages and Structure

The app will have seven HTML template files in total, all stored inside a `templates` folder. There will be a `base.html` file which acts as the parent template containing the navbar and footer so I do not have to repeat that code on every page. All other pages will extend this base template. The `home.html` page is the landing page and the first thing a user sees when they visit the site. The `recipes.html` page is the main feature of the app where users can search and browse dishes. There will also be a `favourites.html` page where logged in users can view the recipes they have saved. There will be a dedicated `signup.html` page for new users and a separate `login.html` page for returning users. Once authenticated, users will have access to a `profile.html` page which also contains the option to log out. Finally there will be an `about.html` page that explains what GlobalGrub is.

For the static files, there will be a `static` folder in the root of the project. Inside `static` there will be a `css` folder containing a file called `style.css` where all of the custom CSS will be written. There will also be a `js` folder inside `static` containing a file called `script.js` where all of the `JavaScript` will be written. Any images used in the project, including the preset avatar icons, will be stored in an `images` folder inside `static` as well.

## Authentication and the Login System

One of the main things I want to implement is a proper login system using `Flask Sessions`. When a user signs up on the `Sign Up` page, their username and password will be saved to a `users.json` file, which acts as a simple storage system without needing a full database. Passwords will be securely hashed so they are never stored as plain text. When users log in through the `Login` page, `Flask` will check their credentials against the JSON file, and if they match, a session will be created for them.

The navigation bar will change depending on whether the user is logged in or not. Guests will see `Sign Up` and `Login` links, while authenticated users will see `Profile` and `Logout` links. This will be handled using `Flask`'s templating system in the `base.html` template by checking if there is an active session. This makes the same template behave differently depending on who is viewing it.

## Guest vs Logged In Experience

Guests will still be able to browse recipes without signing up. They can search, filter, and view dishes, but they won't be able to save anything or access the `Favourites` page. If a guest tries to go to `Favourites`, they will see a message prompting them to log in. Once logged in, the `Favourites` page unlocks and shows their saved recipes. This encourages sign ups without forcing them.

## The Recipes Page

The `Recipes` page is the most complex part of the app. At the top there will be a search bar that connects to `TheMealDB API`, which returns meal data including names, images, ingredients, and instructions. When a user types in a search term and submits, `Flask` will make a request to the API on the backend and pass the results back to the template to display as recipe cards.

Underneath the search bar, there will be a filtering system using dropdowns for `categories`, `regions`, and `ingredients`. This allows users to narrow down results based on the type of dish or cuisine. 

Below the search and filters there will be a curated carousel section. This will be hardcoded with dishes from `European`, `American`, and `Asian` cuisines. For each region, I will include popular top dishes. Each dish will have a category heading (Meat, Fish, Vegetarian and Dessert) an image, a title, and a link to a reputable external website for the full recipe. Hardcoding this section ensures quality and relevance.

## The Favourites Page

The `Favourites` page will be a gallery of recipe cards saved by logged in users. JavaScript and `localStorage` will handle saving and removing favourites on the client side. When a logged in user clicks a save button on a recipe card, the recipe data will be stored in `localStorage`. `Flask` will confirm the user is logged in through the session, and then JavaScript will retrieve the saved items for display. Guests will see a locked version with a prompt to log in.

## The Profile Page and Avatar System

The `Profile` page will be a dashboard for logged in users. It will show their username, current avatar, and stats like the number of recipes saved. A logout button will clear the session and redirect to `Home`.

The avatar picker will include 10 preset food-themed icons. A modal will allow users to select an avatar. Selection will save to `localStorage` and update in the navbar and profile page instantly without refreshing.

## CSS Styling

All styling will be written in `style.css` in `static/css`. It will be linked in `base.html` across all pages. The design will be warm, inviting, and modern, using `flexbox` and `CSS grid` for layout. Transitions and hover effects will make the interface interactive.

## JavaScript

All interactive behaviour will be handled in `script.js` in `static/js`. This includes:

- Carousel logic on the `Recipes` page  
- Avatar modal for selection and saving  
- `localStorage` operations for favourites and avatars  
- Dynamic UI updates like toggling save button state and darkmode 

## Flask and Python

`app.py` will define all routes, handling `GET` and `POST` requests as needed. `Flask` will also manage `TheMealDB API` requests and pass the data to templates. `Users.json` will store accounts with hashed passwords.

## File Structure

Root of project: `app.py`, `users.json`, `requirements.txt`, `render.yaml`  
templates/: `base.html`, `home.html`, `recipes.html`, `favourites.html`, `signup.html`, `login.html`, `profile.html`, `about.html`  
static/: `css/style.css`, `js/script.js`, `images/` for avatars and other images  

## Deployment

The app will be deployed on `Render.com` connected to `GitHub`. The start command will use `gunicorn` to run the Flask app. Environment variables will be configured on Render for session security.