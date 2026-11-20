"""Runs all diagrams. Right-click this file in PyCharm > Run 'main'."""
import binary_tree
import graph
import dfs_methods

if __name__ == "__main__":
    root = binary_tree.build_tree()
    print("=== Binary Tree ===")
    print("BFS:", " - ".join(binary_tree.bfs(root)))
    print("DFS:", " - ".join(binary_tree.dfs(root)))

    g = graph.build_graph()
    print("\n=== Graph ===")
    print("BFS:", " - ".join(graph.bfs(g, "S")))
    print("DFS:", " - ".join(graph.dfs(g, "S")))

    name_root = dfs_methods.build_name_tree()
    print("\n=== DFS Methods in Tree: LINUS KERK SIAROT (Assessment 3.6) ===")
    print("Preorder :", " - ".join(dfs_methods.preorder(name_root)))
    print("Inorder  :", " - ".join(dfs_methods.inorder(name_root)))
    print("Postorder:", " - ".join(dfs_methods.postorder(name_root)))
