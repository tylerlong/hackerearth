n = int(input())
board = [[0 for c in range(n)] for r in range(n)]

def print_board():
    for r in board:
        print(' '.join(str(c) for c in r))

def attacked(r, c, board):
    for r1 in range(n):
        for c1 in range(n):
            if board[r1][c1] == 1:
                if r1 == r:
                    return True
                if c1 == c:
                    return True
                if c1 + r1 == c + r:
                    return True
                if c1 - r1 == c - r:
                    return True
    return False

def n_queues(board, n, r0 = -1, c0 = -1):
    if n == 0:
        return board
    for r in range(len(board)):
        for c in range(len(board)):
            if r < r0 or (r == r0 and c <= c0):
                continue
            if attacked(r, c, board):
                continue
            board[r][c] = 1
            if n_queues(board, n - 1, r, c) != False:
                return board
            board[r][c] = 0
    return False

if n_queues(board, n) == False:
    print('NO')
else:
    print('YES')
    print_board()
