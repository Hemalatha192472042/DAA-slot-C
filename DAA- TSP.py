INF = 999999


def tsp(graph, n):
    dp = [[INF] * n for _ in range(1 << n)]

    dp[1][0] = 0

    for mask in range(1 << n):
        for current in range(n):

            if not (mask & (1 << current)):
                continue

            for next_city in range(n):

                if mask & (1 << next_city):
                    continue

                new_mask = mask | (1 << next_city)

                dp[new_mask][next_city] = min(
                    dp[new_mask][next_city],
                    dp[mask][current] + graph[current][next_city]
                )

    final_mask = (1 << n) - 1

    answer = INF

    for city in range(1, n):
        answer = min(
            answer,
            dp[final_mask][city] + graph[city][0]
        )

    return answer


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)

print("Minimum cost =", tsp(graph, n))
