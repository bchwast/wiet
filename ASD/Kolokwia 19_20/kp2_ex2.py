from kp2_ex2_testy import runtests
from queue import PriorityQueue


def let( ch ): return ord(ch) - ord("a")


def find_word(G, W, s):
    Q = PriorityQueue()
    Q.put((0, s, 0))

    m = float("inf")
    while not Q.empty():
        cost, u, ind = Q.get()
        if ind == len(W) - 1:
            m = min(m, cost)
        else:
            for v in range(len(G[u][1])):
                if G[u][1][v][2] == W[ind + 1]:
                    Q.put((cost + G[u][1][v][1], G[u][1][v][0], ind + 1))
    return m


def letters( G, W ):
    n = len(G[0])
    graph = [[None, []] for _ in range(n)]
    for i in range(n):
        graph[i][0] = G[0][i]
    for i in range(len(G[1])):
        graph[G[1][i][0]][1].append((G[1][i][1], G[1][i][2], G[0][G[1][i][1]]))
        graph[G[1][i][1]][1].append((G[1][i][0], G[1][i][2], G[0][G[1][i][0]]))

    m = float("inf")
    for i in range(n):
        if graph[i][0] == W[0]:
            m = min(m, find_word(graph, W, i))

    if m == float("inf"):
        return -1
    return m
    

runtests( letters )
    
    
