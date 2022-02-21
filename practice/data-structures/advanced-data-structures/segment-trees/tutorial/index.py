from collections import deque
import sys

inputs = deque(line.strip() for line in sys.stdin)
(n, q) = (int(i) for i in inputs.popleft().split(' '))
l = [int(i) for i in inputs.popleft().split(' ')]

class Node:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.mid = (start + end) // 2
        if end - start == 1:
            self.data = l[start]
        else:
            self.left = Node(start, self.mid)
            self.right = Node(self.mid, end)
            self.data = min(self.left.data, self.right.data)
    def update(self, index: int, value: int):
        if self.end - self.start == 1:
            self.data = value
        else:
            if index >= self.mid:
                self.right.update(index, value)
            else:
                self.left.update(index, value)
            self.data = min(self.left.data, self.right.data)
    def query(self, start: int, end: int) -> int:
        if start == self.start and end == self.end:
            return self.data
        if start >= self.mid:
            return self.right.query(start, end)
        if end <= self.mid:
            return self.left.query(start, end)
        return min(self.left.query(start, self.mid), self.right.query(self.mid, end))

root = Node(0, n)

while len(inputs) > 0:
    line = inputs.popleft()
    (start, end) = (int(i) for i in line[2:].split(' '))
    if line.startswith('q'):
        print(root.query(start - 1, end))
    elif line.startswith('u'):
        root.update(start - 1, end)
