def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return False

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

    return True


def boruvka(edges, vertices):
    parent = list(range(vertices))
    rank = [0] * vertices

    num_components = vertices
    mst = []
    total = 0

    while num_components > 1:

        cheapest = [None] * vertices

        for u, v, weight in edges:
            set_u = find(parent, u)
            set_v = find(parent, v)

            if set_u != set_v:
                if cheapest[set_u] is None or \
                   weight < cheapest[set_u][2]:
                    cheapest[set_u] = (u, v, weight)

                if cheapest[set_v] is None or \
                   weight < cheapest[set_v][2]:
                    cheapest[set_v] = (u, v, weight)

        for edge in cheapest:
            if edge is not None:
                u, v, weight = edge

                if union(parent, rank, u, v):
                    mst.append(edge)
                    total += weight
                    num_components -= 1

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

boruvka(edges, 4)
