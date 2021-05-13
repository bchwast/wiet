# za każdym razem bierzemy najcięższy przedmiot, który jesteśmy w stanie wziąć


def trailer_loading(W, K):
    n = len(W)
    W.sort(reverse=True)
    result = []
    for i in range(n):
        if W[i] <= K:
            result.append(W[i])
            K -= W[i]
    return result


W = [2, 2, 4, 8, 1, 8, 16]
K = 27
print(trailer_loading(W, K))