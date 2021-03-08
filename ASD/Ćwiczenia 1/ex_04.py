def minmax(T):
    n = len(T)
    el_min = T[n-1]
    el_max = T[n-1]
    for i in range(0, n-1, 2):
        if T[i] > T[i+1]:
            T[i], T[i+1] = T[i+1], T[i]
        if T[i+1] > el_max:
            el_max = T[i+1]
        if T[i] < el_min:
            el_min = T[i]
    return el_min, el_max

T = [34, 700, 2, 344, 100, 124, 1000]
print(minmax(T))