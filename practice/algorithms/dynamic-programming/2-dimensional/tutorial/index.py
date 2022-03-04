from collections import deque
import sys

inputs = deque([int(n) for n in line.strip().split(' ')] for line in sys.stdin)
(rows, cols) = inputs.popleft()

matrix = []
for row in range(rows):
  matrix.append(inputs.popleft())

results = [[0] * cols for _ in range(rows)]
results[0][0] = matrix[0][0]
for row in range(1, rows):
  results[row][0] = results[row - 1][0] + matrix[row][0]
for col in range(1, cols):
  results[0][col] = results[0][col - 1] + matrix[0][col]
for row in range(1, rows):
  for col in range(1, cols):
    results[row][col] = results[row - 1][col] + results[row][col - 1] - results[row - 1][col -1] + matrix[row][col]

[queries] = inputs.popleft()
for query in range(queries):
  (row, col) = inputs.popleft()
  print(results[row - 1][col - 1])
