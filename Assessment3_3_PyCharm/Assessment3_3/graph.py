r"""
Assessment 3.3: Non-Linear Data Structure
Diagram 2: Graph (Name: SIAROT)

       S
      / \
     I   A
    / \ /
   R   O
    \ /
     T

Edges: S-I, S-A, I-R, I-O, A-O, R-T, O-T

ALGORITHM D - Build the graph
    1. Create an empty adjacency list for S, I, A, R, O, T.
    2. For each edge (u, v): add v to u's neighbors and u to v's neighbors.

ALGORITHM E - BFS (queue)
    1. Add the start vertex to the queue and mark it visited.
    2. While the queue is not empty:
         remove the front vertex and visit it;
         add every unvisited neighbor to the queue and mark it visited.

ALGORITHM F - DFS (recursion)
    1. DFS(vertex): mark vertex visited and visit it.
    2. For each unvisited neighbor, call DFS(neighbor).
"""
from collections import deque


def build_graph():
    edges = [("S", "I"), ("S", "A"), ("I", "R"), ("I", "O"),
             ("A", "O"), ("R", "T"), ("O", "T")]
    graph = {v: [] for v in "SIAROT"}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def bfs(graph, start):
    visited, result, queue = {start}, [], deque([start])
    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


def dfs(graph, vertex, visited=None, result=None):
    if visited is None:
        visited, result = set(), []
    visited.add(vertex)
    result.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
    return result


if __name__ == "__main__":
    graph = build_graph()
    print("Graph")
    print("BFS:", " - ".join(bfs(graph, "S")))
    print("DFS:", " - ".join(dfs(graph, "S")))
