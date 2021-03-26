def binarysearch(T, wanted, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if T[mid] == wanted:
        return True
    elif T[mid] > wanted:
        return binarysearch(T, wanted, low, mid - 1)
    else:
        return binarysearch(T, wanted, mid + 1, high)


def partition(T, low, high):
    pivot = T[high]
    i = low - 1
    for j in range(low, high):
        if T[j] <= pivot:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i + 1], T[high] = T[high], T[i + 1]
    return i + 1


def quicksort(T, low, high):
    while low < high:
        mid = partition(T, low, high)
        if mid - low < high - mid:
            quicksort(T, low, mid - 1)
            low = mid + 1
        else:
            quicksort(T, mid + 1, high)
            high = mid - 1


def if_sums(T):
    quicksort(T, 0, len(T) - 1)
    flag = True

    curr = False
    for i in range(1, len(T) - 2):
        if binarysearch(T, T[0] - T[i], i, len(T) - 1):
            curr = True
            break
    if not curr:
        return False

    for i in range(1, len(T) - 2):
        curr = False
        for j in range(i):
            if binarysearch(T, T[i] - T[j], 0, i - 1) or binarysearch(T, T[i] - T[j], i + 1, len(T) - 1):
                curr = True
                break
        if not curr:
            return False

    curr = False
    for i in range(len(T) - 3):
        if binarysearch(T, T[len(T) - 1] - T[i], i, len(T) - 2):
            curr = True
            break
    if not curr:
        return False

    return True


T = [2, 1, 0, 1, 0, 0]
print(if_sums(T))