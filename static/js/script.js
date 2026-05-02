/**
 * Project Name: [Global Grub]
 * License: MIT
 * Copyright (c) 2026 [Colm Nolan]
 */

(() => {
    "use strict";

    // Hamburger menu toggle
    const hamburger = document.querySelector(".hamburger");
    const mobileMenu = document.querySelector(".mobile-menu");

    if (hamburger && mobileMenu) {
        hamburger.addEventListener("click", () => {
            mobileMenu.classList.toggle("open");
            document.body.classList.toggle("menu-open");

            const isOpen = mobileMenu.classList.contains("open");
            hamburger.setAttribute("aria-expanded", String(isOpen));
            mobileMenu.setAttribute("aria-hidden", String(!isOpen));
        });

        // Close mobile menu when a link is clicked
        mobileMenu.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                mobileMenu.classList.remove("open");
                document.body.classList.remove("menu-open");
                hamburger.setAttribute("aria-expanded", "false");
                mobileMenu.setAttribute("aria-hidden", "true");
            });
        });
    }

    // Country search functionality
    const countrySearch = document.getElementById("country-search");
    const countryLinks = document.querySelectorAll(".country-link");
    const noResults = document.getElementById("no-countries");

    // Filter country links based on search input
    if (countrySearch && countryLinks.length) {
        countrySearch.addEventListener("input", () => {
            const searchTerm = countrySearch.value.toLowerCase().trim();
            // Track if any country links are visible after filtering
            let isVisible = false;

            countryLinks.forEach((link) => {
                const countryName = link.textContent.toLowerCase().trim();

                if (countryName.includes(searchTerm)) {
                    link.style.display = "";
                    isVisible = true;
                } else {
                    link.style.display = "none";
                }
            });

            if (noResults) {
                if (isVisible) {
                    noResults.style.display = "none";
                } else {
                    noResults.style.display = "block";
                }
            }

        });
    }

    // Search input clear button functionality
    const searchForm = document.getElementById("searchForm");
    const searchInput = document.getElementById("mealSearch");
    const clearBtn = document.getElementById("clear-button");

    if (searchForm && searchInput && clearBtn) {
        clearBtn.style.display = "none";

        // Show spinner when form is submitted
        searchForm.addEventListener("submit", () => {
            const spinner = document.getElementById("loading-spinner");
            const resultsArea = document.querySelector(".search-results");

            // Show the loading spinner
            if (spinner) {
                spinner.classList.remove("hidden");
                spinner.setAttribute("aria-hidden", "false");
            }

            // Dim the previous results area while loading
            if (resultsArea) {
                resultsArea.style.opacity = "0.3";
                // Disable pointer events to prevent interaction with old results
                resultsArea.style.pointerEvents = "none";
                resultsArea.setAttribute("aria-busy", "true");
            }
        });

        // Show clear button when user types in the search input
        searchInput.addEventListener("input", () => {
            if (searchInput.value.trim() !== "") {
                clearBtn.style.display = "block";
            } else {
                clearBtn.style.display = "none";
            }
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
    const passwordInput = document.getElementById("password");

    if (eyeIcon && passwordInput) {
        eyeIcon.addEventListener("click", () => {
            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                eyeIcon.classList.add("open");
                eyeIcon.classList.remove("closed");
                eyeIcon.setAttribute("aria-label", "Hide password");
                eyeIcon.setAttribute("aria-pressed", "true");
            } else {
                passwordInput.type = "password";
                eyeIcon.classList.add("closed");
                eyeIcon.classList.remove("open");
                eyeIcon.setAttribute("aria-label", "Show password");
                eyeIcon.setAttribute("aria-pressed", "false");
            }
        });
    }

})();