def transitive_closure(graph):
    V = len(graph)
    closure = [[0] * V for _ in range(V)]

    # Initialize closure matrix as the input adjacency matrix
    for i in range(V):
        for j in range(V):
            closure[i][j] = graph[i][j]

    # Warshall's Algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure

# Given relation as an adjacency matrix (1-based indexing converted to 0-based)
graph = [
    [0, 0, 0, 1],  # 1 → 4
    [1, 0, 1, 0],  # 2 → 1, 2 → 3
    [0, 0, 0, 1],  # 3 → 4
    [0, 0, 0, 0]   # 4 has no outgoing edges
]

# Compute transitive closure
result = transitive_closure(graph)

# Print result
print("Transitive Closure:")
for row in result:
    print(row)