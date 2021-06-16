from e2_ex1_testy import runtests

def zbycholud(A, F, i, e):
    if F[i][e] != float("inf"):
        return F[i][e]

    res = float("inf")
    for k in range(i):
        if 0 <= e + i - k - A[i] < len(F[k]):
            res = min(res, zbycholud(A, F, k, e + i - k - A[i]))
    F[i][e] = res + 1
    return F[i][e]


def zbigniew(A):
    n = len(A)
    F = [[float("inf")] * (n + 1) for _ in range(n)]
    for e in range(A[0] + 1):
        F[0][e] = 0

    res = float("inf")
    for e in range(n):
        zbycholud(A, F, n - 1, e)
        res = min(res, F[n - 1][e])

    return res
       

runtests( zbigniew ) 
