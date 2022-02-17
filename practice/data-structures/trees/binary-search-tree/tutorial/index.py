from collections import deque
import sys
from typing import Optional

q = deque(line.strip() for line in sys.stdin)

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

def insert(node: Optional[Node], data: int):
    if node == None:
        return Node(data)
    if data <= node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node

n = int(q.popleft())
root: Optional[Node] = None
for data in q.popleft().split(' '):
    root = insert(root, int(data))

def print_node(node: Optional[Node], level: int = 0):
    if node == None:
        return
    print_node(node.right, level + 1)
    print('{indent}==>{data}'.format(indent = ' ' * 4 * level, data = node.data))
    print_node(node.left, level + 1)
print_node(root)
