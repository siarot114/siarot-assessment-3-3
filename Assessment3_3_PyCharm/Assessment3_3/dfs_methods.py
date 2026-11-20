r"""
Assessment 3.6: DFS Methods in Tree
Binary Tree (Name: LINUS KERK SIAROT)
First Name = LINUS KERK, Last Name = SIAROT (second name not included)
Letters are placed level by level, left to right:  LINUSKERKSIAROT

                          L
                 /                 \
              I                       N
          /       \               /       \
         U         S             K         E
       /   \     /   \         /   \     /   \
      R     K   S     I       A     R   O     T

ALGORITHM A - Build the tree
    1. Create a node for each letter of LINUSKERKSIAROT (15 letters).
    2. Set the first letter (L) as the root.
    3. Place the remaining letters level by level, left to right:
       the node at position p gets its left child at 2p and right child at 2p+1.

ALGORITHM B - DFS methods (Preorder, Inorder, Postorder)
    Each method is a recursive function DFS(node):
      1. If node is empty, return (base case).
      2. Otherwise visit the node and its two subtrees in this order:

    PREORDER  (Root -> Left -> Right)
         a. Visit node.
         b. PREORDER(left child).
         c. PREORDER(right child).

    INORDER   (Left -> Root -> Right)
         a. INORDER(left child).
         b. Visit node.
         c. INORDER(right child).

    POSTORDER (Left -> Right -> Root)
         a. POSTORDER(left child).
         b. POSTORDER(right child).
         c. Visit node.

    Expected output:
         Preorder : L - I - U - R - K - S - S - I - N - K - A - R - E - O - T
         Inorder  : R - U - K - I - S - S - I - L - A - K - R - N - O - E - T
         Postorder: R - K - U - S - I - S - I - A - R - K - O - T - E - N - L
"""
from binary_tree import Node

NAME = "LINUSKERKSIAROT"


def build_name_tree(letters=NAME):
    """Build a complete binary tree, placing letters level by level."""
    nodes = [Node(c) for c in letters]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]


def preorder(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.value)          # Root
    preorder(node.left, result)        # Left
    preorder(node.right, result)       # Right
    return result


def inorder(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    inorder(node.left, result)         # Left
    result.append(node.value)          # Root
    inorder(node.right, result)        # Right
    return result


def postorder(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    postorder(node.left, result)       # Left
    postorder(node.right, result)      # Right
    result.append(node.value)          # Root
    return result


if __name__ == "__main__":
    root = build_name_tree()
    print("DFS Methods in Binary Tree (LINUS KERK SIAROT)")
    print("Preorder :", " - ".join(preorder(root)))
    print("Inorder  :", " - ".join(inorder(root)))
    print("Postorder:", " - ".join(postorder(root)))
