from e1_ex3_testy import runtests
from math import log


def insertionsort(T):
    for i in range(1, len(T)):
        el = T[i]
        j = i - 1
        while j >= 0 and T[j] > el:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = el


def bucketsort(T):
    maxEl, minEl = max(T), min(T)
    bucketTab = [[] for _ in range(len(T))]
    bucketRange = (maxEl - minEl) / len(T)
    for i in range(len(T)):
        bucketTab[min(int((T[i] - minEl) / bucketRange), len(T) - 1)].append(T[i])

    for i in range(len(T)):
        insertionsort(bucketTab[i])

    ind = 0
    for i in range(len(T)):
        for j in range(len(bucketTab[i])):
            T[ind] = bucketTab[i][j]
            ind += 1

                 
    
def fast_sort(tab, a):
    n = len(tab)
    T = [log(tab[i], a) for i in range(n)]
    bucketsort(T)
    for i in range(n):
        tab[i] = a ** T[i]
    return tab



runtests( fast_sort )
