def solve_n_queen(n):
    """Solve the N-Queen problem for a given board size."""
    def is_safe(board, row, col):
        # Check vertical attack
        for i in range(row):
            if board[i][col] == 1:
                return False
        # Check diagonal attack (left and right)
        for i in range(1, row + 1):
            if col - i >= 0 and board[row - i][col - i] == 1:
                return False
            if col + i < n and board[row - i][col + i] == 1:
                return False
        return True

    def solve(board, row):
        if row == n:
            solution = []
            for r in board:
                solution.append("".join("Q" if x == 1 else "." for x in r))
            results.append(solution)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    results = []
    board = [[0] * n for _ in range(n)]
    solve(board, 0)
    return results
