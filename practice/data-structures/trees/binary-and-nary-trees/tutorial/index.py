import sys
from collections import deque

class Node:
    def __init__(self):
        self.left = None
        self.right = None

lines = deque(line.strip() for line in sys.stdin)

(n, _) = lines.popleft().split(' ')

root = Node()

while len(lines) > 0:
    path_str = lines.popleft()
    data = lines.popleft()
    node = root
    for c in path_str:
        if c == 'L':
            if node.left == None:
                node.left = Node()
            node = node.left
        elif c == 'R':
            if node.right == None:
                node.right = Node()
            node = node.right

def height(node):
    if node == None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def diameter(root):
    if root == None:
        return 0
    return max(
        diameter(root.left), 
        diameter(root.right), 
        height(root.left) + 1 + height(root.right)
    )

print(diameter(root))
