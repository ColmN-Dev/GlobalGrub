(() => {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('mealSearch');
    const clearBtn = document.getElementById("clear-button");

    if (!searchForm || !searchInput || !clearBtn) {
        return;
    }

    clearBtn.style.display = "none";

    // Show clear button when user types in the search input
    searchInput.addEventListener("input", () => {
        if (searchInput.value.trim() !== "") {
            clearBtn.style.display = "block";
        } else {
            clearBtn.style.display = "none";
        }
    });

    // Clear search input and hide clear button when clicked
    clearBtn.addEventListener("click", () => {
        searchInput.value = "";
        clearBtn.style.display = "none";
    });

    // Clear search input when Escape key is pressed
    searchInput.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
        searchInput.value = "";
        clearBtn.style.display = "none";
        }
    });

    // Prevent form submission if search input is empty
    searchForm.addEventListener("submit", (e) => {
        if (searchInput.value.trim() === "") {
            e.preventDefault();
        }
    });

})();