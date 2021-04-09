def amazon(T):
    n = len(T)
    possibilities = [0] * n
    possibilities[n - 1] = 1

    for i in range(n - 2, -1, -1):
        for j in range(i, min(i + T[i] + 1, n)):
            possibilities[i] += possibilities[j]

    return possibilities[0]


T = [2, 1, 3, 2, 1, 0]
print(amazon(T))