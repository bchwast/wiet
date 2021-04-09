def binary_search(T, indexes, low, high, wanted):
    while high - low > 1:
        mid = low + (high - low) // 2
        if T[indexes[mid]] >= wanted:
            high = mid
        else:
            low = mid
    return high


def lis(T):
    tail_indexes = [0] * (len(T) + 1)
    parent_indexes = [-1] * (len(T) + 1)
    length = 1

    for i in range(1, len(T)):
        if T[i] < T[tail_indexes[0]]:
            tail_indexes[0] = i
        elif T[i] > T[tail_indexes[length - 1]]:
            parent_indexes[i] = tail_indexes[length - 1]
            tail_indexes[length] = i
            length += 1
        else:
            pos = binary_search(T, tail_indexes, -1, length - 1, T[i])
            parent_indexes[i] = tail_indexes[pos - 1]
            tail_indexes[pos] = i

    return length, tail_indexes[length - 1], parent_indexes


def print_solution(T, parent, i):
    if parent[i] != -1:
        print_solution(T, parent, parent[i])
    print(T[i])

T = [2, 5, 3, 7, 11, 8, 10, 13, 6]
res, ind, parents = lis(T)
print(res, "\n")
print_solution(T, parents, ind)