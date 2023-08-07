// Get the input field element
var inputField = document.getElementById('inputField');

// Add event listener for focus event
inputField.addEventListener('focus', function(event) {
    // Scroll to the focused input field when virtual keyboard appears
    event.target.scrollIntoView({ behavior: 'smooth', block: 'center' });
});