# tankujemy tyle, żeby móc dojechać do stacji o najtańszej benzynie, jeżeli nasz bak nie ma takiej pojemności, żeby móc
# dotrzeć do stacji o najtańszej benzynie lub jesteśmy na takiej stacji to tankujemy do pełna


def tank(S, P, L, t):
    n = len(S) + 2
    stations = [[None, None] for _ in range(n)]
    stations[0][0], stations[0][1] = 0, 0

    for i in range(1, n - 1):
        stations[i][0], stations[i][1] = S[i - 1], P[i - 1]
    stations[n - 1][0], stations[n - 1][1] = t, float("inf")

    fuel = 0
    cost = 0
    for i in range(n - 1):
        if i > 0:
            fuel -= (stations[i][0] - stations[i - 1][0])
        min_cost = stations[i][1]
        st = i
        for j in range(i, n):
            if stations[j][0] > stations[i][0] + L:
                break
            else:
                if stations[j][1] < min_cost:
                    min_cost, st = stations[j][1], j
        if st == i:
            cost += min(L - fuel, (t - stations[i][0]) - fuel) * stations[i][1]
            fuel = L
        else:
            cost += max(((stations[st][0] - stations[i][0]) - fuel) * stations[i][1], 0)
            fuel = max(fuel, stations[st][0] - stations[i][0])

    return cost

S = [5, 8, 12, 15, 27, 30, 43, 50]
P = [6, 2, 4, 256, 3, 65, 12, 1]
t = 56
L = 15
print(tank(S, P, L, t))


