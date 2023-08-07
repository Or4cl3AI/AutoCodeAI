// Toggle section visibility
var sectionToggleButton = document.querySelector('.section-toggle-button');
var section = document.querySelector('.section');

sectionToggleButton.addEventListener('click', function(event) {
    section.classList.toggle('active');
});