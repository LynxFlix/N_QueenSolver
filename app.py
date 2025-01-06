from flask import Flask, render_template, request

app = Flask(__name__)

# N-Queens solver logic
def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, row, n, solutions):
    # Base case: if all queens are placed, add the solution
    if row == n:
        solution = [row[:] for row in board]
        solutions.append(solution)
        return

    # Try placing a queen in all columns of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve():
    try:
        # Get the board size from the user
        size = int(request.form["size"])
        if size < 4:
            return render_template("result.html", error="N must be greater than or equal to 4.")

        # Solve the N-Queens problem and get all solutions
        solutions = solve_nqueens(size)
        return render_template("result.html", solutions=solutions, count=len(solutions), n=size)

    except Exception as e:
        return render_template("result.html", error=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
