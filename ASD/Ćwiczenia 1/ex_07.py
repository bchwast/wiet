def sumElements(T, x):
    n = len(T)

    for i in range(n):
        for j in range(n):
            if i != j:
                if T[i] + T[j] == x:
                    return True

    return False


T = [4, 2, 3, 6, 2, 8, 3, 65, 32, 6]
print(sumElements(T, 0))