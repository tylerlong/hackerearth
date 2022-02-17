from collections import deque
import sys
from typing import Optional

q = deque(line.strip() for line in sys.stdin)

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

def insert(node: Optional[Node], data: int) -> Node:
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

def print_node(node: Optional[Node], level: int = 0) -> None:
    if node == None:
        return
    print_node(node.right, level + 1)
    print('{indent}==>{data}'.format(indent = ' ' * 4 * level, data = node.data))
    print_node(node.left, level + 1)
# print_node(root)

query = int(q.popleft())

def find_node(node: Optional[Node], data: int) -> Optional[Node]:
    if node == None:
        return None
    if node.data == data:
        return node
    return find_node(node.left, data) or find_node(node.right, data)

def traverse_node(node: Optional[Node]) -> None:
    if node == None:
        return
    print(node.data)
    traverse_node(node.left)
    traverse_node(node.right)
traverse_node(find_node(root, query))
