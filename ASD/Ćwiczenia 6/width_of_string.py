def width_of_string(S, t):
    n = len(t)
    F = [float("-inf")] * (n + 1)

    for i in range(n + 1):
        for s in S:
            substr = t[i - len(s): i]
            if i > len(s):
                if s == substr:
                    F[i] = max(F[i], min(len(s), F[i - len(s)]))
            elif i == len(s):
                if s == substr:
                    F[i] = max(F[i], len(s))

    return F[n]


S = ["ab", "abab", "ba", "bab", "b"]
t = "ababbab"
print(width_of_string(S, t))