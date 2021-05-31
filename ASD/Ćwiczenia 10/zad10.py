from copy import deepcopy
from queue import PriorityQueue


def max_extending_path( G, s, t ):
    def relax(u, v, weight):
      if d[v] < min(d[u], weight):
        d[v] = min(d[u], weight)
        parent[v] = u
        return True
      return False

    def path(u):
      if parent[u] is None:
        return [u]
      return path(parent[u]) + [u]

    n = len(G)
    d = [float("-inf")] * n
    parent = [None] * n
    Q = PriorityQueue()

    d[s] = float("inf")
    Q.put((d[s], s))
    while not Q.empty():
      u = Q.get()[1]
      for v in G[u]:
        if relax(u, v[0], v[1]):
          Q.put((d[v[0]], v[0]))

    route = path(t)
    # print(d)
    return route
    return []
  

  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1,4), (2,3)], # 0
     [(3,2)], # 1
     [(3,5)], # 2
     []] # 3
s = 0
t = 3
C = 3  


GG = deepcopy( G )
path = max_extending_path( GG, s, t )

print("Sciezka :", path)


if path == []: 
  print("Błąd (1): Spodziewano się ścieżki!")
  exit(0)
  
if path[0] != s or path[-1] != t: 
  print("Błąd (2): Zły początek lub koniec!")
  exit(0)

  
capacity = float("inf")
u = path[0]
  
for v in path[1:]:
  connected = False
  for (x,c) in G[u]:
    if x == v:
      capacity = min(capacity, c)
      connected = True
  if not connected:
    print("Błąd (3): Brak krawędzi ", (u,v))
    exit(0)
  u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
  print("Błąd (4): Niezgodna pojemność")
else:
  print("OK")
  
