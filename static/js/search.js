(async () => {

    // Get key elements from the page
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('recipeSearch');
    const results = document.getElementById('results');
    const hint = document.getElementById('clear-hint');

    // Clears the search input and results
    const clearSearch = () => {
        searchInput.value = '';
        results.innerHTML = '';
        searchInput.blur();
    };

    // Handle search form submission
    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const value = searchInput.value.trim();
        results.innerHTML = "";

        // If input is empty, prompt user to enter something
        if (!value) {
            results.innerHTML = `<p class="empty-search">Enter a recipe to search.</p>`;
            return;
        }

        // Show hint to clear search (if element exists)
        if (hint) {
            hint.textContent = "Press Esc to clear";
            hint.classList.remove("message-fade-out");

            // Fade out hint after a short delay
            setTimeout(() => {
                hint.classList.add("message-fade-out");
            }, 3000);
        }

        // Show loading message while fetching data
        results.innerHTML = `<p class="loading">Loading...</p>`;

        try {
            // Fetch recipes from TheMealDB API based on search term
            const res = await fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${value}`);
            const data = await res.json();

            // Clear loading message
            results.innerHTML = "";

            // If no recipes found, show message
            if (!data.meals) {
                results.innerHTML = `<p class="empty-search">No recipes found.</p>`;
                return;
            }

            // Limit results to 12 for cleaner layout
            data.meals.slice(0, 12).forEach(meal => {

                // Create card container
                const card = document.createElement('div');
                card.className = 'recipe-card';

                // Recipe title
                const title = document.createElement('h3');
                title.textContent = meal.strMeal;

                // Recipe image
                const img = document.createElement('img');
                img.src = meal.strMealThumb;
                img.alt = meal.strMeal;
                img.loading = "lazy";

                // Link to recipe detail page (handled in Flask)
                const link = document.createElement('a');
                link.href = `/recipe/${meal.idMeal}`;
                link.appendChild(img);

                // Additional info (region + category)
                const meta = document.createElement('p');
                meta.className = 'recipe-meta';
                meta.textContent = `${meal.strArea} • ${meal.strCategory}`;

                // Build and display the card
                card.append(title, link, meta);
                results.appendChild(card);
            });

        } catch (err) {
            console.error(err);
            results.innerHTML = `<p class="error">Error fetching recipes. Try again.</p>`;
        }
    });

    // Clear search when navigating back
    window.addEventListener('popstate', clearSearch);

    // Allow user to press Escape to clear search
    searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            clearSearch();
            searchInput.focus();
        }
    });

})();
