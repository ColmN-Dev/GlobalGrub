(() => {
    "use strict";

    // Hamburger menu toggle
    const hamburger = document.querySelector(".hamburger");
    const mobileMenu = document.querySelector(".mobile-menu");

    if (hamburger && mobileMenu) {
        hamburger.addEventListener("click", () => {
            mobileMenu.classList.toggle("open");
            document.body.classList.toggle("menu-open");
        });

        // Close mobile menu when a link is clicked
        mobileMenu.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                mobileMenu.classList.remove("open");
                document.body.classList.remove("menu-open");
            });
        });
    }

    // Search input clear button functionality
    const searchForm = document.getElementById("searchForm");
    const searchInput = document.getElementById("mealSearch");
    const clearBtn = document.getElementById("clear-button");

    if (searchForm && searchInput && clearBtn) {
        clearBtn.style.display = "none";

        // Show clear button when user types in the search input
        searchInput.addEventListener("input", () => {
            clearBtn.style.display = searchInput.value.trim() !== "" ? "block" : "none";
        });

        // Clear search input and hide clear button when clicked
        clearBtn.addEventListener("click", (e) => {
            e.preventDefault();
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
    }

    // Password visibility toggle
    const eyeIcon = document.getElementById("togglePassword");
    const input = document.getElementById("password");

    if (eyeIcon && input) {
      eyeIcon.addEventListener("click", () => {
          if (input.type === "password") {
              input.type = "text";
              eyeIcon.classList.add("open");
              eyeIcon.classList.remove("closed");
        } else {
            input.type = "password";
            eyeIcon.classList.add("closed");
            eyeIcon.classList.remove("open");
        }
      });
    }

})();