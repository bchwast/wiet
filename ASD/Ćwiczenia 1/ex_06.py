def binarySearch(T, el, a, b):
    if a > b:
        return None
    c = (a+b)//2
    if T[c] == el:
        key = binarySearch(T, el, a, c-1)
        if key == None:
            return c
        return key
    elif T[c] > el:
        return binarySearch(T, el, a, c-1)
    else:
        return binarySearch(T, el, c+1, b)


T = [0, 1, 2, 2, 3, 3, 4, 5]
print(binarySearch(T, 3, 0, len(T)-1))