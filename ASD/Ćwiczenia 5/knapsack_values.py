def knapsack(W, P, MaxW):
    n = len(W)
    Psum = 0
    Wsum = 0
    for i in range(n):
        Psum += P[i]
        Wsum += W[i]

    F = [[[-1, -1] for _ in range(Psum + 1)] for _ in range(n)]
    for p in range(Psum - P[0] + 1):
        F[0][p][0], F[0][p][1] = Wsum - W[0], Psum - P[0]
    for p in range(Psum, Psum - P[0], -1):
        F[0][p][0], F[0][p][1] = Wsum, Psum
    for i in range(1, n):
        F[i][Psum][0], F[i][Psum][1] = Wsum, Psum

    for i in range(1, n):
        for p in range(Psum - 1, -1, -1):
            if F[i - 1][p][1] - P[i] < p:
                if F[i - 1][p][0] < F[i][p + 1][0]:
                    F[i][p] = F[i - 1][p]
                else:
                    F[i][p] = F[i][p + 1]
            else:
                if F[i - 1][p][0] - W[i] < F[i][p + 1][0]:
                    F[i][p][0] = F[i - 1][p][0] - W[i]
                    F[i][p][1] = F[i - 1][p][1] - P[i]
                else:
                    F[i][p] = F[i][p + 1]

    i = Psum
    while F[n - 1][i][0] > MaxW:
        i -= 1

    return F[n - 1][i][1]


P = [21, 3, 6, 3, 87, 34, 7, 34, 97, 34]
W = [4, 5, 12, 9, 1, 13, 2, 5, 2, 5]
MaxW = 30
print(knapsack(W, P, MaxW))