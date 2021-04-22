# f(i, w, h) - największy zysk jaki można uzyskać spośród przedmiotów od 0 do i nie przekraczając wagi w i wysokości h

# f(0, w, h) = {0    ; w(0) > W || h(0) > H
#            = {v(0) ; w(0) <= W && h(0) <= H

# f(i, 0, h) = f(i, w, 0) = f(i, 0, 0) = 0

# f(i, w, h) = max(f(i - 1, w, h), f(i - 1, w - w(i), h - h(i)) + v(i))  ; w >= w(i) && h >= h(i)


def get_solution(F, v, w, h, i, w_i, h_i):
    if i == 0:
        if w_i >= w[0] and h_i >= h[0]:
            return [0]
        return []

    if w_i >= w[i] and h_i >= h[i] and F[i][w_i][h_i] == F[i - 1][w_i - w[i]][h_i - h[i]] + v[i]:
        return get_solution(F, v, w, h, i - 1, w_i - w[i], h_i - h[i]) + [i]
    return get_solution(F, v, w, h, i - 1, w_i, h_i)


def knapsack(v, w, h, W, H):
    n = len(v)
    F = [[[0] * (H + 1) for _ in range(W + 1)] for _ in range(n)]

    for w_i in range(w[0], W + 1):
        for h_i in range(h[0], H + 1):
            F[0][w_i][h_i] = v[0]

    for i in range(1, n):
        for w_i in range(1, W + 1):
            for h_i in range(1, H + 1):
                F[i][w_i][h_i] = F[i - 1][w_i][h_i]
                if w_i >= w[i] and h_i >= h[i]:
                    F[i][w_i][h_i] = max(F[i][w_i][h_i], F[i - 1][w_i - w[i]][h_i - h[i]] + v[i])

    return F[n-1][W][H], F


v = [4, 3, 5, 3, 3, 4, 5, 32]
w = [5, 2, 4, 6, 4, 2, 5, 6]
h = [1, 2, 4, 3, 1, 3, 4, 2]
W = 10
H = 5
res, F = knapsack(v, w, h, W, H)
print(res, get_solution(F, v, w, h, len(v) - 1, W, H))