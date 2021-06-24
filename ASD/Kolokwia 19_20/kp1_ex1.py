
from kp1_ex1_testy import runtests


def min_d(d, enqueued, n):
    best = float("inf")
    for u in range(n):
        if d[u] < best and enqueued[u]:
            best = d[u]
            vert = u
    return vert


def dijkstra(G, s, t):
    def path(u):
        if parent[u] is None:
            return [u]
        return path(parent[u]) + [u]


    n = len(G)
    d = [(float("inf"))] * n
    parent = [None] * n
    enqueued = [True] * n

    d[s] = 0
    for i in range(n):
        u = min_d(d, enqueued, n)
        enqueued[u] = False

        for v in range(n):
            if 0 <= G[u][v] and d[u] + G[u][v] < d[v] and enqueued[v]:
                d[v] = G[u][v] + d[u]
                parent[v] = u

    route = path(t)
    return route


def jak_dojade(G, P, d, a, b):
    n = len(G)
    big_G = [[-1] * ((d + 1) * n) for _ in range((d + 1) * n)]
    for u in range(n):
        for v in range(n):
            for i in range(d + 1):
                if G[u][v] > -1 and G[u][v] <= i:
                    big_G[u + (i * d)][]




    return None

        

runtests( jak_dojade ) 
