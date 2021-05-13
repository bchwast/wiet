def binary_search(T, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if T[mid] == x:
            return mid
        elif T[mid] > x:
            return binary_search(T, low, mid - 1, x)
        else:
            return binary_search(T, mid + 1, high, x)
    else:
        return False