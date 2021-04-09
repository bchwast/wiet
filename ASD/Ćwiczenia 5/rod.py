def rod(price, n):
    profit = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            profit[i] = max(profit[i], price[j] + profit[i - j])

    return profit[n]


price = [0, 2, 2, 7, 5, 3]
print(rod(price, 5))