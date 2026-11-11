"""Runs both diagrams. Right-click this file in PyCharm > Run 'main'."""
import binary_tree
import graph

if __name__ == "__main__":
    root = binary_tree.build_tree()
    print("=== Binary Tree ===")
    print("BFS:", " - ".join(binary_tree.bfs(root)))
    print("DFS:", " - ".join(binary_tree.dfs(root)))

    g = graph.build_graph()
    print("\n=== Graph ===")
    print("BFS:", " - ".join(graph.bfs(g, "S")))
    print("DFS:", " - ".join(graph.dfs(g, "S")))
