def coin_change(coins, target):
    solutions = [float("inf")] * (target + 1)
    solutions[0] = 0

    for i in range(1, target + 1):
        for c in range(len(coins)):
            if i - coins[c] >= 0:
                result = solutions[i - coins[c]]

                if result != float("inf"):
                    solutions[i] = min(solutions[i], result + 1)

    if solutions[target] != float("inf"):
        return solutions[target]
    return -1


coins = [1, 3, 5, 7]
print(coin_change(coins, 1))