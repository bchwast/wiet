# sortujemy zadania nierosnąco po zyskach, bierzemy zadanie o największym zysku i wykonujemy je w najpóźniejszym
# możliwym terminie


class Task:
    def __init__(self, i, d, g):
        self.i = i
        self.d = d
        self.g = g

    def __repr__(self):
        return f"({self.i}, d={self.d}, g={self.g})"

    def __str__(self):
        return f"({self.i}, d={self.d}, g={self.g})"


def tasks(T, deadline):
    T.sort(key=lambda x: x.d)
    result = [Task("mock", i, float("-inf")) for i in range(deadline)]

    for i in range(len(T)):
        if T[i].d < deadline + 1:
            j = T[i].d - 1
            while j >= 0:
                if result[j].g < T[i].g:
                    result[j] = T[i]
                    break
                j -= 1

    return result


T = [Task(1, 4, 5), Task(2, 4, 7), Task(3, 2, 2), Task(4, 1, 4), Task(5, 5, 8), Task(6, 3, 4)]
deadline = 5
print(tasks(T, deadline))