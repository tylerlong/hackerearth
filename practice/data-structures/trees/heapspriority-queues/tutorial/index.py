from collections import deque
import sys

inputs = deque(line.strip() for line in sys.stdin)
inputs.popleft() # size

r = max([int(i) for i in inputs.popleft().split(' ')])
inputs.popleft() # number of queries

while(len(inputs) > 0):
    q = inputs.popleft()
    if q.startswith('1 '):
        r = max(r, int(q[2:]))
    elif q == '2':
        print(r)
