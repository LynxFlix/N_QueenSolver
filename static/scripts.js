// Script to enhance user experience with simple animations
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector('form');
    const solutionsContainer = document.querySelector('.solutions-container');

    // Alert user when form is submitted
    if (form) {
        form.addEventListener('submit', function () {
            alert("Solving the N-Queens problem. Please wait...");
        });
    }

    // Optionally, you can add animations here when the solutions appear
});
