from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Function to solve the N-Queens problem
def solve_nqueens(n):
    """
    Solves the N-Queens problem using a backtracking algorithm.
    
    :param n: The size of the chessboard (number of queens).
    :return: A list of lists representing the board with the queen's positions (1 for queen, 0 for empty).
    """
    board = [[0] * n for _ in range(n)]  # Create an empty n x n chessboard
    
    # Helper function to check if it's safe to place a queen at position (row, col)
    def is_safe(board, row, col):
        # Check this column on the upper side
        for i in range(row):
            if board[i][col] == 1:
                return False
        
        # Check the upper left diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check the upper right diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 1:
                return False
        
        return True
    
    # Recursive function to solve the problem using backtracking
    def solve(board, row):
        if row >= n:
            return True  # All queens are placed
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1  # Place the queen
                
                if solve(board, row + 1):
                    return True  # Move to the next row if placement is safe
                
                board[row][col] = 0  # Backtrack if placement didn't lead to a solution
        
        return False  # No safe place for a queen in this row
    
    if solve(board, 0):
        return board  # Return the board with queens placed
    
    return None  # Return None if no solution exists

# Flask route for rendering the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Flask route to handle solving the N-Queens problem
@app.route('/solve', methods=['POST'])
def solve():
    try:
        size = int(request.form['size'])  # Getting the board size from the form
        solution = solve_nqueens(size)  # Calling the solve_nqueens function
        
        if solution:
            return jsonify({'solution': solution})
        else:
            return jsonify({'error': 'No solution found for the given board size.'})
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter a valid integer for N.'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
