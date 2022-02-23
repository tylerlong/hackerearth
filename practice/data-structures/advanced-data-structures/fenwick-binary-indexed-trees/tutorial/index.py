from collections import deque
import sys

inputs = deque(line.strip() for line in sys.stdin)
inputs.popleft()
arr = [int(i) for i in inputs.popleft().split(' ')]
inputs.popleft()

def gcd(i: int, j: int) -> int:
    if j % i == 0:
        return i
    return gcd(j % i, i)

def f(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        sum += gcd(i, n)
    return sum

while len(inputs) > 0:
    line = inputs.popleft()
    (i, j) = (int(i) for i in line[2:].split(' '))
    if line.startswith('U '):
        arr[i - 1] = j
    elif line.startswith('C '):
        sum = 0
        for i in range(i, j + 1):
            sum += f(arr[i - 1])
        print(sum)
