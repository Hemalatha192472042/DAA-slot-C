def bellman_ford(graph, V, source):
    dist = [float('inf')] * V
    dist[source] = 0

    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Negative weight cycle exists")
            return

    print("Shortest distances:")
    for i in range(V):
        print(source, "->", i, "=", dist[i])


graph = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -3),
    (2, 3, 4),
    (1, 3, 5)
]

bellman_ford(graph, 4, 0)
