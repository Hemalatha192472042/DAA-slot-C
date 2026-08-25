def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(edges, vertices):
    edges.sort(key=lambda x: x[2])

    parent = list(range(vertices))
    rank = [0] * vertices

    mst = []
    total = 0

    for u, v, weight in edges:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            mst.append((u, v, weight))
            total += weight
            union(parent, rank, x, y)

    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)

    print("Total cost:", total)


edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

kruskal(edges, 4)
