n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

def print_board():
    for r in board:
        print(' '.join(str(c) for c in r))

def attacked(r, c):
    for r1 in range(n):
        for c1 in range(n):
            if board[r1][c1] == 1:
                if r == r1:
                    return True
                if c == c1:
                    return True
                if r + c == r1 + c1:
                    return True
                if r - c == r1 - c1:
                    return True
    return False

def n_queens(q, r0 = 0, c0 = 0):
    if q == 0:
        return True
    for r in range(r0, n):
        for c in range(n):
            if r == r0 and c < c0:
                continue
            if attacked(r, c):
                continue
            board[r][c] = 1
            if n_queens(q - 1, r, c):
                return True
            board[r][c] = 0
    return False

if n_queens(n):
    print('YES')
    print_board()
else:
    print('NO')
