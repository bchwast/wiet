def optimal_strategy(T):
    n = len(T)
    solutions = [[0] * n for _ in range(n)]

    for gap in range(n):
        for right in range(gap, n):
            left = right - gap

            l2r = 0
            if left + 2 <= right:
                l2r = solutions[left + 2][right]

            l1r1 = 0
            if left + 1 <= right - 1:
                l1r1 = solutions[left + 1][right - 1]

            lr2 = 0
            if left <= right - 2:
                lr2 = solutions[left][right - 2]

            solutions[left][right] = max(T[left] + min(l2r, l1r1), T[right] + min(l1r1, lr2))

    return solutions[0][n - 1]


T = [2, 3, 1, 4, 6, 8, 1, 2]
print(optimal_strategy(T))