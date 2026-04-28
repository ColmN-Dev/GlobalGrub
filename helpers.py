# Project Name: [Global Grub]
# License: MIT
# Copyright (c) 2026 [Colm Nolan]

import requests


def get_meal_by_id(meal_id):
    """Fetch a single meal from TheMealDB by ID. Returns meal dict or None."""
    try:
        url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
        response = requests.get(url, timeout=10)
        data = response.json()
        meals = data.get("meals")
        if meals:
            return meals[0]
        return None
    except Exception:
        return None
