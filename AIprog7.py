#7. Model and solve a Constraint Satisfaction Problem (CSP) using the N-Queens problem.
N = 4

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve_n_queens(board, row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col

            if solve_n_queens(board, row + 1):
                return True

            board[row] = -1

    return False

board = [-1] * N

if solve_n_queens(board, 0):
    print("Solution for", N, "Queens:")
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print()
else:
    print("No solution exists")

'''
Solution for 4 Queens:
- Q - - 
- - - Q 
Q - - - 
- - Q - 
'''