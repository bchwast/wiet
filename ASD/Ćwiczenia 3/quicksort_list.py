class Node:
    def __init__(self):
        self.value = None
        self.next = None


def tab2list(T):
    head = Node()
    tail = head
    for i in range(len(T)):
        el = Node()
        el.value = T[i]
        tail.next = el
        tail = el
    return head.next


def printList(L):
    while L != None:
        print(L.value, end=" -> ")
        L = L.next
    print("|")


def getTail(L):
    if L == None or L.next == None:
        return L

    prev = None
    while L != None:
        prev = L
        L = L.next

    return prev


def partition(L, pivot):
    smaller = Node()
    tail_s = smaller
    equal = Node()
    tail_e = equal
    larger = Node()
    tail_l = larger

    while L != None:
        if L.value < pivot.value:
            tail_s.next = L
            tail_s = tail_s.next
        elif L.value == pivot.value:
            tail_e.next = L
            tail_e = tail_e.next
        else:
            tail_l.next = L
            tail_l = tail_l.next
        L = L.next

        tail_s.next = None
        tail_e.next = None
        tail_l.next = None

    return smaller, tail_s, equal.next, tail_e, larger, tail_l


def quicksort(Head, Tail):
    if Head == Tail:
        return Head, Tail

    sHead, sTail, eHead, eTail, lHead, lTail = partition(Head, Head)

    if sHead == sTail:
        sHead = eHead
        sTail = eHead
    else:
        sHead = sHead.next
        sHead, sTail = quicksort(sHead, sTail)
        sTail.next = eHead

    if lHead == lTail:
        lHead = eTail
        lTail = eTail
    else:
        lHead = lHead.next
        lHead, lTail = quicksort(lHead, lTail)
        eTail.next = lHead

    return sHead, lTail


def qsort(L):
    if L == None:
        return None

    l = getTail(L)
    L, _ = quicksort(L, l)
    return



#T = [324, 76, 567, 3, 64, 6, 2, 324, 2, 45, 512, 5, 6345, 57, 35]
T = [-20, 456,7,457, 75,4, 6, -235,-435,436,235,66,4,357,623,6,-56789,6,7,346,34,36,36,436,36, 10, 2, 4, 0, 2, 5, -1, 4, -2, -5, 3]
L = tab2list(T)
printList(L)
l = getTail(L)
printList(l)
qsort(L)
printList(L)
