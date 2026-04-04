# GlobalGrub

## Overview

GlobalGrub is a Flask web application built to allow users to discover and browse recipes from cuisines around the world. It includes user authentication, a profile system with a custom avatar picker, and the ability to save favourite recipes. The focus of the project is on combining a Python backend with a polished, fully custom frontend UI.

---

## Features

- Search functionality using the `TheMealDB` API
- Curated regional carousel showcasing top dishes from Asian, European, and American cuisines
- User authentication (sign up, login, logout)
- Save favourite recipes stored in `SQLite` database
- Profile page with stats, edit username, change password, and avatar selection
- PlayStation-style avatar picker modal with preset food-themed icons
- Guest browsing with limited access — full features unlocked on login
- Dynamic navbar that swaps between Sign Up/Login and Profile/Logout based on session state
- Cookie consent banner on first visit
- Responsive design with a slide out mobile menu

---

## Tech Stack

- Backend: `Flask` (`Python`)
- Frontend: `HTML`, custom `CSS`, `JavaScript`
- Database: `SQLite` via `Flask-SQLAlchemy`
- Deployment: `Render.com`

---

## Authentication

Authentication is handled using `Flask Sessions`. User data including username, hashed password, and avatar choice is stored in a `SQLite` database managed by `Flask-SQLAlchemy`. Saved favourites are linked to each user via a foreign key relationship between the `Users` and `Favourites` tables.

---

## Status

This project is currently in development as part of a Python module assignment.