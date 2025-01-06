# N-Queens Problem Solver

## Overview
The **N-Queens Problem** is a famous problem in computer science where the goal is to place N queens on an NxN chessboard such that no two queens threaten each other. A queen can attack another queen if they are on the same row, column, or diagonal.

This project provides a solution to the N-Queens problem using a backtracking algorithm, implemented as a web application with Flask for the backend and HTML, CSS, and JavaScript for the frontend.

## Features
- Solve the N-Queens problem for any `N ≥ 4`.
- Display all possible solutions as visually formatted chessboards.
- Easy-to-use web interface to enter the size of the chessboard.
- Displays all possible solutions (for example, for N=8, it shows 92 solutions).
- Provides a clean and modern UI with animations and styling for both input and result display.

## Technologies Used
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Algorithm**: Backtracking


## Installation

To run this project locally, follow these steps:

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/N-queen_solver.git
    ```

2. Navigate into the project directory:
    ```bash
    cd N-queen_solver
    ```

3. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the Flask application:
    ```bash
    python app.py
    ```

7. Open your browser and visit:
    ```
    http://127.0.0.1:5000
    ```

## How It Works

- **Backend Logic**: 
  The backend is built using **Flask**, a Python web framework. The core logic for solving the N-Queens problem is implemented in `solver.py`, which uses a **backtracking algorithm** to find all solutions. The `solve_nqueens(n)` function is called to find all valid board configurations for a given `N`.

- **Frontend Interaction**:
  The user is presented with a form on the homepage (`index.html`), where they can input the size `N` of the chessboard. When the user submits the form, a POST request is sent to the server, which calculates the solutions and returns them to the frontend in a JSON format. The results are then displayed on the `result.html` page as chessboards.

- **CSS and Styling**:
  The chessboard and the entire page are styled using CSS, making it more user-friendly and visually appealing.

## Usage

1. **Input**: Enter the desired value of `N` (e.g., 4, 8, 10) and click the "Solve" button to get all the possible solutions for that N value.

2. **Display**: After solving, the results are displayed on the **result page** as visually formatted chessboards. Each valid solution will be shown as a grid with queens placed in the correct positions (marked as `Q`).

3. **Error Handling**:
    - If the input is not a valid integer, an error message will be displayed.
    - If `N` is less than 4, it will notify the user that there are no valid solutions for smaller values of `N`.

## Example

For `N = 4`, the two solutions would be displayed as:


and


For `N = 8`, the page will display 92 solutions, each formatted as a chessboard.

## Future Enhancements

- **Performance Optimization**: As the value of `N` increases, the number of solutions increases exponentially. Caching solutions or limiting the number of displayed solutions can improve performance.
- **Visualization Enhancements**: Add animations to visualize how queens are placed on the board.
- **Other Chessboard Variants**: Extend the application to solve other chessboard-based problems, such as the N-Rooks problem or the N-Knights problem.
- **Mobile Responsiveness**: Improve the responsiveness of the design for mobile and tablet screens.

## Contributing

Feel free to fork this project and submit pull requests if you'd like to contribute. If you find any bugs or issues, open an issue in the GitHub repository, and I'll get back to you as soon as possible!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- This project was inspired by the classic N-Queens problem, which is commonly used to teach backtracking algorithms in computer science.
- Thanks to Flask documentation and various online resources for help with web development and problem-solving strategies.


