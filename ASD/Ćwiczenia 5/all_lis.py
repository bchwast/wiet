def lis(T):
    longest = [1] * len(T)
    children = [[] for _ in range(len(T))]

    for i in range(len(T) - 1, -1, -1):
        for j in range(i + 1, len(T)):
            if T[j] > T[i] and longest[j] + 1 >= longest[i]:
                if longest[j] + 1 > longest[i]:
                    longest[i] = longest[j] + 1
                    children[i].clear()
                children[i].append(j)

    return max(longest), longest, children


def printAllLIS(T):
    cnt = 0
    def get_solution(T, children, seq, ind, i):
        nonlocal cnt
        if ind == 1:
            seq[len(seq) - ind] = T[i]
            for i in range(len(seq)):
                print(seq[i], end=" ")
            print()
            cnt += 1
            return

        seq[len(seq) - ind] = T[i]
        for j in range(len(children[i])):
            get_solution(T, children, seq, ind - 1, children[i][j])


    res, longest, children = lis(T)
    seq = [-1] * res
    for ind in range(len(T)):
        if longest[ind] == res:
            get_solution(T, children, seq, res, ind)

    return cnt


T = [2, 1, 4, 3]

res, longest, parents = lis(T)
# print(parents)
print(printAllLIS(T))