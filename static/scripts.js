// Handling the form submission
document.getElementById('sizeForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const size = document.getElementById('size').value;

    // Clear previous results
    const boardContainer = document.getElementById('board');
    boardContainer.innerHTML = '';
    const message = document.getElementById('message');
    message.textContent = '';

    // Fetch solutions from the backend
    fetch('/solve', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `size=${size}`
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                message.textContent = data.error;
                message.classList.add('error');
            } else {
                displaySolutions(data.solutions, data.count);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            message.textContent = 'Something went wrong. Please try again.';
            message.classList.add('error');
        });
});

// Function to display all solutions dynamically
function displaySolutions(solutions, count) {
    const boardContainer = document.getElementById('board');
    const message = document.getElementById('message');

    if (solutions.length === 0) {
        message.textContent = 'No solutions found for the given board size.';
        message.classList.add('error');
        return;
    }

    message.textContent = `${count} solutions found! Scroll to explore.`;
    message.classList.add('success');

    // Display each solution as a chessboard
    solutions.forEach((solution, index) => {
        const solutionWrapper = document.createElement('div');
        solutionWrapper.classList.add('solution-wrapper');

        const title = document.createElement('h3');
        title.textContent = `Solution ${index + 1}`;
        solutionWrapper.appendChild(title);

        const table = document.createElement('table');
        table.classList.add('chessboard');

        solution.forEach(row => {
            const tr = document.createElement('tr');
            row.forEach(cell => {
                const td = document.createElement('td');
                if (cell === 1) {
                    td.classList.add('queen');
                }
                tr.appendChild(td);
            });
            table.appendChild(tr);
        });

        solutionWrapper.appendChild(table);
        boardContainer.appendChild(solutionWrapper);
    });
}
