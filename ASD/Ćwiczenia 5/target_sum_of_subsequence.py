def tssum(T, target):
    n = len(T)
    F = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        F[i][0] = True

    for i in range(1, target + 1):
        F[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < T[i - 1]:
                F[i][j] = F[i - 1][j]
            else:
                F[i][j] = (F[i - 1][j] or F[i - 1][j - T[i - 1]])

    for i in range(n + 1):
        for j in range(target + 1):
            print(F[i][j], end =" ")
        print()

    return F[n][target]


T = [3, 34, 4, 12, 5, 2]
print(tssum(T, 9))