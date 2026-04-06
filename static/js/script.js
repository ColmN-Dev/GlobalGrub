const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');

hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
});

function toggleMenu() {
    document.querySelector('.mobile-menu').classList.toggle('open');
}

const links = mobileMenu.querySelectorAll("a");

links.forEach(link => {
    link.addEventListener("click", () => {
        mobileMenu.classList.remove("open");
    });
});
