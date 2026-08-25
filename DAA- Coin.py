def coin_greedy(coins, amount):
    coins.sort(reverse=True)

    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    print("Coins used:", result)
    print("Number of coins:", len(result))


coins = [1, 2, 5, 10, 20, 50]
amount = 93

coin_greedy(coins, amount)
