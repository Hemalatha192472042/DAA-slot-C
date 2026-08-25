import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    pq = [(0, source)]

    while pq:
        current_distance, current = heapq.heappop(pq)

        if current_distance > distances[current]:
            continue

        for neighbor, weight in graph[current]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    print("Shortest distances:")
    for node in distances:
        print(source, "->", node, "=", distances[node])


graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

dijkstra(graph, 0)
