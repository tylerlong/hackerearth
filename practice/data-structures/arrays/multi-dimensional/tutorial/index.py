import sys

lines = [line.strip() for line in sys.stdin]
[rows, cols] = [int(item) for item in lines[0].split(' ')]

arr = []
for line in lines[1:]:
    arr.append(line.split(' '))

for col in range(cols):
    print(' '.join([arr[row][col] for row in range(rows)]))
