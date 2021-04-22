# f(i, e) - minimalna ilość skoków, które Zbigniew musi wykonać, żeby dostać się od 0 do i posiadając e energii

# f(i + k, e - k + A[i + k]) = min(f(i + k, e - k + A[i + k]), f(i, e) + 1) ; 0 <= k < e
# f(0, j) = 0 ; 0 <= j <= A[0]
# w p. p. - f(i, e) = inf


def zbigniew(A):
    n = len(A)

    F = [[float("inf")] * (n + 1) for _ in range(n)]
    for e in range(A[0] + 1):
        F[0][e] = 0

    for i in range(n):
        for e in range(1, n + 1):
            if F[i][e] != float("inf"):
                for k in range(e):
                    if i + k < n and e - k + A[i + k] <= n:
                        F[i + k][e - k + A[i + k]] = min(F[i + k][e - k + A[i + k]], F[i][e] + 1)

    res = float("inf")
    for e in range(n + 1):
        res = min(res, F[n-1][e])

    return res


A = [4, 5, 2, 4, 1, 2, 1, 0]
print(zbigniew(A))