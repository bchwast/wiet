from queue import Queue
from math import sqrt

# tworzymy graf, w któym wyspy są wierzchołkami, pomiędzy wierzchołkami, które są we wzajemnej odległości <= Z wstawiamy
# krawędź o wadze 1, a pomiędzy tymi, które są we wzajemnej odległości > Z, ale <= 2Z wstawiamy krawędź o wadze 2.
# puszczamy bfs'a z wyspy startowej, jeżeli ściągneliśmy wierzchołek wrzucony z wagą 2, to wrzucamy go spowrtem do kolejki
# z wagą 1


def dst(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def make_graph(W, Z):
    n = len(W)
    G = [[] for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            if a != b:
                d = dst(W[a], W[b])
                if d <= Z:
                    G[a].append((b, 1))
                    G[b].append((a, 1))
                elif Z < d <= 2 * Z:
                    G[a].append((b, 2))
                    G[b].append((a, 2))
    return G


def sailor(W, Z):
    G = make_graph(W, Z)
    n = len(G)
    visited = [False] * n
    day = [-1] * n
    Q = Queue()
    Q.put((0, 1))
    visited[0] = True
    day[0] = 0

    while not Q.empty():
        u = Q.get()
        if u[1] == 2:
            Q.put((u[0], 1))
        else:
            if u[0] == n - 1:
                return day[n - 1]
            for v in G[u[0]]:
                if not visited[v[0]]:
                    visited[v[0]] = True
                    day[v[0]] = day[u[0]] + v[1]
                    Q.put(v)

    return None


W = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
print(sailor(W, 2))