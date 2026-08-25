import heapq

def prim(graph):
    visited = set()
    mst = []
    pq = [(0, 0, -1)]
    total = 0

    while pq:
        weight, node, parent = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        total += weight

        if parent != -1:
            mst.append((parent, node, weight))

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (w, neighbor, node))

    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)

    print("Total cost:", total)


graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 1)],
    3: [(0, 6), (1, 8), (2, 1)]
}

prim(graph)
