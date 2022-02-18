from collections import deque
import sys
from typing import Dict

inputs = deque(line.strip() for line in sys.stdin)
(n, q) = (int(i) for i in inputs.popleft().split(' '))

dict: Dict[str, int] = {}
for i in range(n):
    line = inputs.popleft()
    [word, weight] = line.split(' ')
    weight = int(weight)
    for i in range(len(word)):
        key = line[:i+1]
        if key in dict:
            dict[key] = max(dict[key], weight)
        else:
            dict[key] = weight

for i in range(q):
    line = inputs.popleft()
    if line in dict:
        print(dict[line])
    else:
        print(-1)