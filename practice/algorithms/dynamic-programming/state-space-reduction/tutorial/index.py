import sys
from collections import deque

inputs = deque([int(i) for i in line.strip().split(' ')] for line in sys.stdin)

[n, minN, maxN] = inputs.popleft()
arr = inputs.popleft()

dp = [[[0] * maxN for _ in range(minN)] for _ in range(n)]
dp[0][0][0] = 1
dp[1][0][0] = 1
dp[2][0][0] = 1


x = 0
y = 0
for i in range(2, len(arr)):
  if arr[i] > arr[i - 1] and arr[i - 1] < arr[i - 2]: # min
    dp[i][x+1][y] += 1
    pass
  elif arr[i] < arr[i - 1] and arr[i - 1] > arr[i - 2]: # max
    dp[i][x][y + 1] += 1

# Not finished yet!
