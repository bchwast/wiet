def maximin(T, k):
    F = [[float("-inf")] * len(T) for _ in range(k)]

    temp = 0
    for i in range(len(T)):
        temp += T[i]
        F[0][i] = temp

    for m in range(1, k):
        for p in range(m, len(T)):
            c_sum = 0
            for i in range(p - 1, m - 2, -1):
                c_sum += T[i + 1]
                F[m][p] = max(F[m][p], min(F[m - 1][i], c_sum))

    return F[k - 1][len(T) - 1]


T = [1, 2, 3, 4, 5]
k = 3
print(maximin(T, k))