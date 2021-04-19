from math import *


def distance(a, b):
    return sqrt(((a[1] - b[1]) * (a[1] - b[1])) + ((a[2] - b[2]) * (a[2] - b[2])))


def tspf(i, j, F, D):
    if F[i][j] != float("inf"):
        return F[i][j]

    if i == j - 1:
        best = float("inf")
        for k in range(j - 1):
            best = min(best, tspf(k, j - 1, F, D) + D[k][j])
        F[j - 1][j] = best
    else:
        F[i][j] = tspf(i, j - 1, F, D) + D[j - 1][j]

    return F[i][j]


def bitonic_tsp(C):
    n = len(C)
    C.sort(key=lambda x: x[1])
    D = [[None] * n for _ in range(n)]
    F = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            D[i][j] = distance(C[i], C[j])

    F[0][1] = D[0][1]

    res = float("inf")
    for i in range(n - 2):
        res = min(res, tspf(i, n - 1, F, D) + D[i][n - 1])

    return res

# C = [["Moskwa", 50, 10], ["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1], ["Olkusz", 2, 1]]

C = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],['I', 0.5, 2.5], ['J', 1.5, 3.5]]
print(bitonic_tsp(C))