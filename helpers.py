# Project Name: [Global Grub]
# License: MIT
# Copyright (c) 2026 [Colm Nolan]

import requests

# Set base URL to avoid repetition in API calls
BASE_URL = "https://www.themealdb.com/api/json/v1/1/"


# Helper functions for calling the API endpoints

def fetch_json(endpoint):
    """Send request to fetch JSON data from the API."""
    try:
        url = BASE_URL + endpoint
        response = requests.get(url, timeout=10)
        # Raise an error for bad HTTP responses (e.g. 404, 500)
        response.raise_for_status()
        
        return response.json()
    
    # Handle JSON parsing errors and print an error message for debugging
    except ValueError:
        print("Error parsing JSON response.")
        return None
    
    # Handle any exceptions that occur during the request and print an error message
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    

def get_meal_by_id(meal_id):
    """Get single meal details by ID."""
    data = fetch_json(f"lookup.php?i={meal_id}")
    meals = data.get("meals") if data else None
    # Return the first meal if it exists, otherwise return None
    return meals[0] if meals else None

def search_meals(search):
    """Search meals by name."""
    data = fetch_json(f"search.php?s={search}")
    # Return the list of meals if it exists, otherwise return an empty list
    return data.get("meals") if data else []

def get_meals_by_region(region):
    """Get meals by region."""
    data = fetch_json(f"filter.php?a={region}")
    return data.get("meals") if data else []

def get_countries():
    """Get list of countries."""
    data = fetch_json("list.php?a=list")
    
    if not data or not data.get("meals"):
        return []
    
    return sorted(
        (item.get("strArea") for item in data["meals"] if item.get("strArea")), 
        key=str.lower
    )