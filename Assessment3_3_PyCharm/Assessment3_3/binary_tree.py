r"""
Assessment 3.3: Non-Linear Data Structure
Diagram 1: Binary Tree (Name: SIAROT)

        S
      /   \
     I     A
    / \   /
   R   O T

ALGORITHM A - Build the tree
    1. Create a node for each letter: S, I, A, R, O, T.
    2. Set S as the root.
    3. I = left of S, A = right of S.
    4. R = left of I, O = right of I.
    5. T = left of A.

ALGORITHM B - BFS (queue)
    1. Create an empty queue and add the root.
    2. While the queue is not empty:
         remove the front node, visit it,
         add its left child, then its right child (if any).

ALGORITHM C - DFS (recursion)
    1. DFS(node): if node is empty, return.
    2. Visit node.
    3. DFS(left child), then DFS(right child).
"""
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    s, i, a, r, o, t = (Node(c) for c in "SIAROT")
    s.left, s.right = i, a
    i.left, i.right = r, o
    a.left = t
    return s


def bfs(root):
    result, queue = [], deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def dfs(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.value)
    dfs(node.left, result)
    dfs(node.right, result)
    return result


if __name__ == "__main__":
    root = build_tree()
    print("Binary Tree")
    print("BFS:", " - ".join(bfs(root)))
    print("DFS:", " - ".join(dfs(root)))
