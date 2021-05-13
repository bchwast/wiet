# sprawdzamy czy będziemy w stanie przelecieć od x do y na pułapie takim jak pułap każdego z połączeń wychodzących z x
# +/- t


def safe_flight(G, x, y, t):
    n = len(G)

    def dfs(G, u, low, high):
        if u == y:
            return True

        visited[u] = True

        for v in G[u]:
            if not visited[v[0]] and low <= v[1] <= high:
                return dfs(G, v[0], low, high)
        return False


    for u in G[x]:
        visited = [False] * n
        visited[x] = True
        if dfs(G, u[0], u[1] - t, u[1] + t):
            return True

    return False


G = [[(1, 10), (5, 3)], [(0, 10), (2, 20), (5, 5)], [(1, 20), (3, 8), (4, 1), (5, 11)], [(2, 8), (4, 3)], [(2, 1), (3, 3), (5, 7)],
     [(0, 3), (1, 5), (2, 11), (4, 7)]]
print(safe_flight(G, 0, 3, 5))