( () => {

  'use strict';
// Hamburger menu toggle
const hamburger = document.querySelector('.hamburger');
const mobileMenu = document.querySelector('.mobile-menu');

if (hamburger && mobileMenu) {
hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
    document.body.classList.toggle('menu-open');
});

mobileMenu.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.remove('open');
    document.body.classList.remove('menu-open');
  });
});
}

})();