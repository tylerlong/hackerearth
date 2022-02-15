n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

def print_board():
    for r in board:
        print(' '.join(str(c) for c in r))

def attackEachOther(r, c, r1, c1):
    if r == r1:
        return True
    if c == c1:
        return True
    if r + c == r1 + c1:
        return True
    if r - c == r1 - c1:
        return True
    return False

stack = []
def attacked(r, c):
    if any(attackEachOther(r, c, r1, c1) for (r1, c1) in stack):
        return True
    return False

def n_queues(q):
    # first round
    for r in range(n):
        for c in range(n):
            if not attacked(r, c):
                board[r][c] = 1
                stack.append((r, c))
                q -= 1
                if q == 0:
                    return True

    while len(stack) > 0:
        # pop and try the next position of it
        (r0, c0) = stack.pop()
        board[r0][c0] = 0
        q += 1
        for r in range(r0, n):
            for c in range(n):
                if r == r0 and c <= c0:
                    continue
                if not attacked(r, c):
                    board[r][c] = 1
                    stack.append((r, c))
                    q -= 1
                    if q == 0:
                        return True
    return False


if n_queues(n):
    print('YES')
    print_board()
else:
    print('NO')
