# Assessment 3.6: DFS Methods in Tree
**Name:** LINUS KERK SIAROT (first name + last name; second name not included)

Letters `LINUSKERKSIAROT` are placed level by level, left to right:

```
                          L
                 /                 \
              I                       N
          /       \               /       \
         U         S             K         E
       /   \     /   \         /   \     /   \
      R     K   S     I       A     R   O     T
```

## Algorithm A: Build the tree
1. Start.
2. Create a node for each letter of LINUSKERKSIAROT.
3. Set the first letter (L) as the root.
4. Place the remaining letters level by level, left to right (the node at position p gets its left child at 2p and its right child at 2p+1).
5. Stop.

## Algorithm B: DFS methods
**DFS(node):** if node is empty, return; otherwise:

| Method | Steps | Result |
|---|---|---|
| Preorder (Root-Left-Right) | Visit node -> Preorder(left) -> Preorder(right) | L - I - U - R - K - S - S - I - N - K - A - R - E - O - T |
| Inorder (Left-Root-Right) | Inorder(left) -> Visit node -> Inorder(right) | R - U - K - I - S - S - I - L - A - K - R - N - O - E - T |
| Postorder (Left-Right-Root) | Postorder(left) -> Postorder(right) -> Visit node | R - K - U - S - I - S - I - A - R - K - O - T - E - N - L |

Program file: `Assessment3_3_PyCharm/Assessment3_3/dfs_methods.py`
