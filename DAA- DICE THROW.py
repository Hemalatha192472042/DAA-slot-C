def dice_throw(dice, faces, target):
    dp = [[0] * (target + 1) for _ in range(dice + 1)]

    dp[0][0] = 1

    for d in range(1, dice + 1):
        for s in range(1, target + 1):
            for f in range(1, faces + 1):
                if s - f >= 0:
                    dp[d][s] += dp[d-1][s-f]

    return dp[dice][target]

print(dice_throw(2, 6, 7))
