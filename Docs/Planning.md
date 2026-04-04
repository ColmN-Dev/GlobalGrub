# GlobalGrub — Project Plan

## What is GlobalGrub?

GlobalGrub is a Flask web application I am building for my Python assignment. The idea behind it is to create a place where users can discover recipes and dishes from different cuisines around the world. I came up with the name because it reflects the global nature of the app and feels catchy and memorable. The app will be built using Flask and Python on the backend, custom CSS for all the styling, and JavaScript for the interactive parts. The finished app will be hosted on Render.com and connected to a GitHub repository.

## Pages and Structure

The app will have eight HTML template files in total, all stored inside a `templates` folder. There will be a `base.html` file which acts as the parent template containing the navbar and footer so I do not have to repeat that code on every page. All other pages will extend this base template. The Home page (`home.html`) is the landing page and the first thing a user sees when they visit the site. The Recipes page (`recipes.html`) is the main feature of the app where users can search and browse dishes. There will also be a Favourites page (`favourites.html`) where logged in users can view the recipes they have saved. There will be a dedicated Sign Up page (`signup.html`) for new users and a separate Login page (`login.html`) for returning users. Once authenticated, users will have access to a Profile page (`profile.html`) which also contains the option to log out. Finally there will be an About page (`about.html`) that explains what GlobalGrub is.

For the static files, there will be a `static` folder in the root of the project. Inside `static` there will be a `css` folder containing a file called `style.css` where all of the custom CSS will be written. There will also be a `js` folder inside `static` containing a file called `script.js` where all of the JavaScript will be written. Any images used in the project, including the preset avatar icons, will be stored in an `images` folder inside `static` as well.

## Database

Instead of using a JSON file to store data, I am going to use `SQLite` as the database and `Flask-SQLAlchemy` to interact with it from Python. `Flask-SQLAlchemy` is an extension that makes it straightforward to define database tables as Python classes and query them without having to write raw SQL. `SQLite` will automatically generate a database file when the app runs for the first time so there is no need to set it up manually. I will only need to install `Flask-SQLAlchemy` using `pip` and import it in `app.py`.

The database will have two tables. The first is a `Users` table which will store each user's `id`, `username`, hashed `password`, and their chosen `avatar`. The second is a `Favourites` table which will store saved recipes, with each row containing a `meal_id`, `meal_name`, `meal_image`, and a `user_id` that links back to the `Users` table as a foreign key. This creates a relationship between the two tables so that each saved recipe is tied to a specific user account.

## Authentication and the Login System

One of the main things I want to implement is a proper login system using Flask `session`. When a user signs up on the Sign Up page, their username and hashed password will be saved to the `SQLite` database. When they log in through the Login page, Flask will check their credentials against the database and if they match it will create a session for them.

The navigation bar will change depending on whether the user is logged in or not. If they are a guest it will show Sign Up and Login links. If they are authenticated it will show Profile and Logout instead. This is something I plan to handle using Flask's templating system in `base.html` by checking if there is an active session. I think this is one of the more interesting parts of the project because it means the same template behaves differently depending on who is looking at it.

## Guest vs Logged In Experience

I want guests to still be able to use the app and browse recipes without having to sign up. They can search and view dishes, but they will not be able to save anything or access the Favourites page. If a guest tries to go to Favourites they will see a message prompting them to log in. Once logged in, the Favourites page unlocks and shows their saved recipes. I think this is a good way to encourage sign ups without forcing people to make an account just to look around.

## The Home Page

The Home page will have a navbar at the top that stays fixed as the user scrolls down. On mobile the navbar will collapse into a hamburger icon that opens a slide out drawer menu from the side. Below the navbar there will be a hero section with a bold headline and short tagline explaining what GlobalGrub is. Underneath that there will be a marquee strip of food images that scrolls continuously using a CSS animation. Below the marquee there will be three large clickable cards representing the three regions — Asian, European, and American — which all link through to the Recipes page. At the bottom of the page will be the footer with links to the main pages of the site and a copyright line. There will also be a cookie consent banner that appears on first visit with a single Accept Necessary Cookies button, since Flask sessions rely on cookies to function.

## The Recipes Page

The Recipes page is the most complex part of the app. At the top there will be a search bar that connects to `TheMealDB` API, which is a free API that returns meal data including names, images, ingredients and instructions. When a user types in a search term and submits, Flask will make a request to the API on the backend and pass the results back to the template to display as recipe cards.

Below the search bar there will be a curated carousel section which will be hardcoded by me with dishes I have researched myself. The carousel will be organised by three world regions: Asian, European, and American. Each region will have eight hardcoded dishes. By default when the page loads the All Regions view is active and the carousel shows 12 dishes in total — one meat dish, one fish dish, one vegetarian dish and one dessert from each of the three regions, giving four dishes per region and twelve overall. When a user clicks on a specific region the JavaScript `updateCarousel` function will filter the display to show all eight dishes from that region only. There will also be an All Regions button that resets back to the default mixed view. Each dish card will have an image, a title, a category label and a link to a reputable external website like BBC Food or AllRecipes where users can get the full recipe.

## The Favourites Page

The Favourites page will be a gallery of recipe cards that the user has saved. Favourites will be stored in the `SQLite` database in the `Favourites` table, linked to the logged in user by their `user_id`. When a logged in user clicks a save button on a recipe card, Flask will write that recipe to the database. When they visit the Favourites page, Flask will query the database for all recipes saved by that user and display them. If the user is not logged in Flask will detect this through the session and render a locked version of the page with a prompt to log in instead.

## The Profile Page

The Profile page will be a dashboard for logged in users. At the top there will be a profile card showing the user's current avatar and their username. Below that there will be a stat showing how many recipes they have saved in their favourites. The page will also have a form to edit their username, a form to change their password, and a button to open the avatar picker modal. There will also be a logout button that clears the session and redirects them to the home page. Any changes to the username or password will be handled as `POST` requests in Flask and will update the relevant fields in the `SQLite` database.

## The Avatar System

I want the avatar picker to work similar to how PlayStation handles profile avatars, where a modal pops up and the user can choose from a set of preset icons. I am planning to have around eight to ten food themed icons to choose from, things like a pizza slice, a taco, a bowl of ramen, a burger and so on. The default will be a plain silhouette icon. When a user picks a new avatar the choice will be saved to their record in the `SQLite` database and the UI will update instantly without needing a full page refresh. The selected avatar will appear in the navbar and on the profile page.

## CSS Styling

All styling for GlobalGrub will be written by me in `style.css` located in the `static/css` folder. I will link this file to every HTML page through `base.html`. I plan to use a range of CSS selectors, classes and IDs to target specific elements across the pages. I will make use of `flexbox` and `CSS grid` for layout, and add transitions and hover effects to make the interface feel interactive and polished. I still need to finalise the colour scheme and font choices but I want the overall feel to be warm and inviting. The fixed navbar, the marquee animation, the slide out mobile menu and the modal will all be styled in this file.

## JavaScript

Most of the interactive behaviour in the app will be handled by `script.js` located in the `static/js` folder. This file will be linked to every HTML page through `base.html` just before the closing `body` tag. The JavaScript will cover the carousel `updateCarousel` function for switching between regions, the slide out mobile hamburger menu, the avatar modal for opening, selecting and updating, the cookie consent banner dismissal, and dynamic UI updates like toggling the save button state on recipe cards. I will also add smooth scrolling and small transitions to make the app feel polished.

## Flask and Python

On the Python side, `app.py` will be the main file where all the routes are defined. I will set up routes for each page and handle both `GET` and `POST` requests where needed. The login, signup, edit username, and change password forms will all use `POST` requests. Flask will also be responsible for making requests to the `TheMealDB` API using the Python `requests` library and passing the data to the templates. I will use Flask's templating system throughout to keep the HTML clean and avoid repeating code.

## File Structure

The root of the project will contain `app.py`, a `globalgrub.db` SQLite database file that is auto generated, `requirements.txt` and a `render.yaml` file for deployment. Inside the root there will be a `templates` folder containing `base.html`, `home.html`, `recipes.html`, `favourites.html`, `signup.html`, `login.html`, `profile.html` and `about.html`. There will also be a `static` folder containing three subfolders. The `css` subfolder will contain `style.css`, the `js` subfolder will contain `script.js`, and the `images` subfolder will contain the preset avatar icons and any other images used throughout the app.

## Deployment

The finished app will be deployed on Render.com. I will connect my GitHub repository to Render and configure the build settings there. The start command will use `gunicorn` to run the Flask app and I will need to set up the necessary environment variables on Render for the session system to work securely.

## Wireframes

The wireframes below were sketched out before building began to plan the layout of the key pages. They cover the Home page, the Recipes page, and the Profile page as these have the most complex layouts. Simpler pages like About, Login, and Sign Up were straightforward enough not to need wireframes.

![Home Page Wireframe](../static/images/wireframes/Home_page.png)

![Recipes Page Wireframe](../static/images/wireframes/Recipes_page.png)

![Profile Page Wireframe](../static/images/wireframes/Profile_page.png)