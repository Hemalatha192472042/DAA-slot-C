def text_justification(words, width):
    n = len(words)

    cost = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        length = 0
        for j in range(i, n):
            length += len(words[j])

            spaces = j - i
            total = length + spaces

            if total <= width:
                extra = width - total

                if j == n - 1:
                    cost[i][j] = 0
                else:
                    cost[i][j] = extra ** 3

    dp = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)
    dp[0] = 0

    for j in range(1, n + 1):
        for i in range(j):
            if cost[i][j - 1] != float('inf'):
                if dp[i] + cost[i][j - 1] < dp[j]:
                    dp[j] = dp[i] + cost[i][j - 1]
                    parent[j] = i

    lines = []
    j = n

    while j > 0:
        i = parent[j]
        lines.append(" ".join(words[i:j]))
        j = i

    lines.reverse()

    print("Justified Text:")
    for line in lines:
        print(line)


words = ["This", "is", "a", "simple", "text", "justification", "problem"]
text_justification(words, 16)
