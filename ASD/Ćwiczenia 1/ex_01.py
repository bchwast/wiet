def insertionSort(T):
    n = len(T)
    for i in range(1, n):
        el = T[i]
        j = i - 1
        while j >= 0 and T[j] > el:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = el
    return T


def selectionSort(T):
    n = len(T)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if T[j] < T[m]:
                m = j
        T[i], T[m] = T[m], T[i]
    return T


def bubbleSort(T):
    n = len(T)
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            if T[j-1] > T[j]:
                T[j-1], T[j] = T[j], T[j-1]
    return T


T = [5, 4, 3, 7, 2, 1]
print(insertionSort(T))
print(selectionSort(T))
print(bubbleSort(T))