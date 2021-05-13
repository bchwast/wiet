# wystarczy zwrócić medianę


def sum_of_distances(A):
    n = len(A)
    if n % 2 == 1:
        return A[(n - 1) // 2]
    return (A[(n - 1) // 2] + A[((n - 1) // 2) + 1]) / 2