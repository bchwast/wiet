# sortujemy punkty z X niemalejąco, początek przedziału kładziemy w pierwszym punkcie, który nie jest zakryty. całość
# powtarzamy aż przykryjemy wszystkie punkty


def singular_ranges_coverage(X):
    X.sort()
    cnt = 1
    i = 1
    dst = X[0] + 1
    while i < len(X):
        if X[i] - dst > 0:
            dst = X[i] + 1
            cnt += 1
        i += 1

    return cnt


X = [0.25, 0.5, 1.6, 3.2, 1.7, 2.9, 5.4, 4.3]
print(singular_ranges_coverage(X))