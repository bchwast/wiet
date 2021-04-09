def palindrome(text):
    n = len(text)

    solutions = [[False] * n for _ in range(n)]

    maxl = 1
    for i in range(n):
        solutions[i][i] = True

    for i in range(n - 1):
        if text[i] == text[i + 1]:
            solutions[i][i + 1] = True
            maxl = 2

    for l in range(3, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1

            if solutions[i + 1][j - 1] and text[i] == text[j]:
                solutions[i][j] = True

                if l > maxl:
                    maxl = l

    return maxl


T = "bee"
print(palindrome(T))
