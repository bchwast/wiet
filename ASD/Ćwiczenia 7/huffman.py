from queue import PriorityQueue
import timeit

# klasa Node do stworzenia drzewa
class Node:
    def __init__(self):
        self.ind = None
        self.left = None
        self.right = None


# funkcja tworząca kody
def c_code(T, node, code):
    # jak dotarliśmy do liścia to możemy odczytać kod i zapisać do tablicy
    if node.ind != None:
        T[node.ind] = code

    # idziemy do lewego poddrzewa i dodajemy 1 do kodu
    if node.left != None:
        c_code(T, node.left, code + "1")

    # idziemy do prawego poddrzewa i dodajemy 0 do kodu
    if node.right != None:
        c_code(T, node.right, code + "0")


# właściwa funkcja
def huffman(S, F):
    n = len(S)
    # tworzymy tablicę dla liści
    nodes = [None] * n
    # tworzymhy tablicę dla kodów
    T = [None] * n
    # inicjalizujemu kolejkę
    huff = PriorityQueue(n)

    # licznik dla wyeliminowania konfliktów w kolejce przy takich samych częstotliwościach
    cnt = 0
    # dla każdego symbolu tworzymy liść i dodajemy go do kolejki
    for i in range(n):
        nodes[i] = Node()
        nodes[i].ind = i
        # (częstoliwość, licznik, node (liść) z symbolem)
        huff.put((F[i], cnt, nodes[i]))
        cnt += 1

    # działamy do momentu aż w kolejce zostanie jeden element
    while huff.qsize() > 1:
        # zdejmujemy z kolejki dwa elementy o najniższej częstotliwości
        a = huff.get()
        b = huff.get()
        # tworzymy node odsyłającego do tamtych dwóch elementów
        root = Node()
        root.left = a[2]
        root.right = b[2]
        # do kolejki dodajemy nowego node'a z częstotliwością będącą sumą częstotliwości dwóch poprzednio zdjętych
        huff.put((a[0] + b[0], cnt, root))
        cnt += 1

    # tworzymy kody
    c_code(T, root, "")

    # zliczamy łączną liczbę bitów potrzebną do wypisania napisu i wypisujemy symbole wraz z kodami
    cost = 0
    for i in range(n):
        print(f"{S[i]} : {T[i]}")
        cost += F[i] * len(T[i])
    # wypisujemy koszt wypisania napisu
    print(f"dlugosc napisu: {cost}")


S = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z']
F = [27, 32, 123, 15, 4, 31, 23, 13, 44, 38, 12, 5, 3, 145, 54, 34, 98, 102, 76, 243, 45, 65, 78]
start = timeit.default_timer()
huffman(S, F)
stop = timeit.default_timer()
print(stop - start)
