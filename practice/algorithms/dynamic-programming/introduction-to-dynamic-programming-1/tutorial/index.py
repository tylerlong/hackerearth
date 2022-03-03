import sys
from collections import deque

inputs = deque(line.strip() for line in sys.stdin)
inputs.popleft()

numbers = [int(i) for i in inputs]
n = max(numbers)
arr = [0] * (n + 1)
arr[1] = 1
arr[2] = 2
arr[3] = 6

for i in range(4, n + 1):
  arr[i] = i * arr[i - 1]

mod = 10 ** 9 + 7
for i in numbers:
  print(arr[i] % mod)
