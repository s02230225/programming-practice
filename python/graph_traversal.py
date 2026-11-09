"""Depth-first traversal of the vertices reachable from a given start."""


def dfs(start, graph):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        stack.extend(reversed(graph.get(vertex, [])))
    return visited


if __name__ == '__main__':
    print(sorted(dfs(0, {0: [1, 2], 1: [2], 2: [0, 3], 3: []})))
