(async () => {
    
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('mealSearch');
    const results = document.getElementById('results');


    // Run search when the form is submitted.
    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const value = searchInput.value.trim();

        // Clear old results before each search.
        results.innerHTML = "";

        // Show a message if the search box is empty.
        if (!value) {
            const p = document.createElement('p');
            p.className = 'empty-search';
            p.textContent = "Enter a meal name to search.";
            results.appendChild(p);
            return;
        }

        try {
            // Fetch matching meals from TheMealDB API.
            const res = await fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${value}`);
            const data = await res.json();

            // Handle searches with no matches.
            if (!data.meals) {
                const p = document.createElement('p');
                p.className = 'empty-search';
                p.textContent = "No results found. Try another search.";
                results.appendChild(p);
                return;
            }

            // Render up to 12 meal cards.
            data.meals.slice(0,12).forEach(meal => {
                const card = document.createElement('div');
                card.className = 'meal-card';

                // Title
                const title = document.createElement('h3');
                title.textContent = meal.strMeal;

                // Image
                const img = document.createElement('img');
                img.src = meal.strMealThumb;
                img.alt = meal.strMeal;
                img.loading = 'lazy';
                img.className = 'meal-thumb';

                // Link to recipe detail page
                const link = document.createElement('a');
                link.href = `/recipe/${meal.idMeal}`;
                link.appendChild(img);

                card.append(title, link);
                results.appendChild(card);
            });

        } catch (err) {
            // Show an error message if the request fails.
            console.error(err);
            results.textContent = "Error fetching data. Try again later.";
        }
    });

            // Function to clear search input and results.
            function clearSearch() {
            input.value = "";
            results.innerHTML = "";
            clearBtn.style.display = "none";
}

            const clearBtn = document.getElementById("clear-button");
            const input = document.getElementById("mealSearch");
            
            // Hide the clear button before search and show it only when there is input.
            clearBtn.style.display = "none";

            // Allow clear button to appear when user types in the search box and hide it when the input is empty.
            input.addEventListener("input", () => {
            if (input.value.trim() !== "") {
                clearBtn.style.display = "block";
            } else {
                clearBtn.style.display = "none";
            }
        });

            clearBtn.addEventListener("click", clearSearch);

            // Press Escape key to clear search input and results.
            input.addEventListener("keydown", (e) => {
            if (e.key === "Escape") {
                clearSearch();
            }
        });


            // Clear search input and results when the clear button is clicked.
            document.getElementById('clear-button').addEventListener('click', (e) => {
                clearSearch();
            });

})();
