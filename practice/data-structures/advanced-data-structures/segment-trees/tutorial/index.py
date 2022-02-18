from collections import deque
import sys

inputs = deque(line.strip() for line in sys.stdin)
inputs.popleft()
l = [int(i) for i in inputs.popleft().split(' ')]
while len(inputs) > 0:
    line = inputs.popleft()
    (start, end) = (int(i) for i in line[2:].split(' '))
    if line.startswith('q'):
        print(min(l[start - 1: end]))
    elif line.startswith('u'):
        l[start - 1] = end
