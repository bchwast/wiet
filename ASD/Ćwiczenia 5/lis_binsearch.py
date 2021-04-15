def get_index(T, low, high, value):
    if 1 < high - low:
        mid = (low + high) // 2
        if T[mid] == value:
            return mid
        elif T[mid] > value:
            return get_index(T, low, mid, value)
        else:
            return get_index(T, mid , high, value)
    return high


def lis(T):
    tails = [-1] * len(T)
    tails[0] = T[0]
    length = 1

    for i in range(len(T)):
        if T[i] < tails[0]:
            tails[0] = T[i]
        elif tails[length - 1] < T[i]:
            tails[length] = T[i]
            length += 1
        else:
            tails[get_index(tails, 0, length - 1, T[i])] = T[i]

    print(tails)
    return length


T = [13, 7, 21, 42, 8, 2, 44, 53]
print(lis(T))
