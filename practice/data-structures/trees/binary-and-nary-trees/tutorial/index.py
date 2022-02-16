import sys
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('\t' * level + '|=====> ' + node.data)
        printTree(node.left, level + 1)

lines = deque(line.strip() for line in sys.stdin)

(n, data) = lines.popleft().split(' ')

root = Node(data)

while len(lines) > 0:
    path_str = lines.popleft()
    data = lines.popleft()
    node = root
    for c in path_str[:-1]:
        if c == 'L':
            node = node.left
        elif c == 'R':
            node = node.right
    if path_str[-1] == 'L':
        node.left = Node(data)
    elif path_str[-1] == 'R':
        node.right = Node(data)

printTree(root)


def diameter(root):
    pass
    # todo
