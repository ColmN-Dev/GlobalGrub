(async () => {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('mealSearch');
    const results = document.getElementById('results');

    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const value = searchInput.value.trim();
        results.innerHTML = "";

        if (!value) {
            const p = document.createElement('p');
            p.className = 'empty-search';
            p.textContent = "Enter a meal name to search.";
            results.appendChild(p);
            return;
        }

        try {
            const res = await fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${value}`);
            const data = await res.json();

            if (!data.meals) {
                const p = document.createElement('p');
                p.className = 'empty-search';
                p.textContent = "No results found. Try another search.";
                results.appendChild(p);
                return;
            }

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
            console.error(err);
            results.textContent = "Error fetching data. Try again later.";
        }
    });
})();
