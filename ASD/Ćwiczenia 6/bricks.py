# zmodyfikowany lis


def bricks(A):
    n = len(A)
    F = [1] * n

    for i in range(1, n):
        for j in range(i):
            if A[j][0] <= A[i][0] and A[i][1] <= A[j][1]:
                F[i] = max(F[j] + 1, F[i])

    return n - F[n - 1]


T = [[1, 10], [2, 5], [2, 7], [5, 8], [5, 6]]
print(bricks(T))
