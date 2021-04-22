# f(i) - maksymalny zysk ze ścięcia drzew od 0 do i

# f(i) = max(f(i - 2) + c[i], f(i - 1)); i >= 2
# f(0) = c[0]
# f(1) = max(c[0], c[1])


def black_forest(C):
    F = [-1] * len(C)
    F[0] = C[0]
    F[1] = max(C[0], C[1])

    for i in range(2, len(C)):
        F[i] = max(F[i - 2] + C[i], F[i - 1])

    return F[len(C) - 1]


T = [4, 2, 5, 10 ,5]
print(black_forest(T))