def cost_of_path(T):
    rows = len(T)
    columns = len(T[0])
    costs = [[0] * columns for _ in range(rows)]

    costs[0][0] = T[0][0]
    for i in range(1, columns):
        costs[0][i] = costs[0][i - 1] + T[0][i]
    for i in range(1, rows):
        costs[i][0] = costs[i - 1][0] + T[i][0]

    for i in range(1, rows):
        for j in range(1, columns):
            costs[i][j] = min(costs[i - 1][j], costs[i][j - 1]) + T[i][j]

    return costs[rows - 1][columns - 1]


T = [[3, 4, 5, 2, 1], [7, 2, 13, 7, 8], [3, 1, 4, 6, 5], [2, 8, 11, 10, 3], [3, 5, 1, 6, 2]]
print(cost_of_path(T))