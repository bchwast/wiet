import timeit

class Node:
  def __init__(self):
    self.val = None
    self.next = None


def tab2list(T):
    head = Node()
    tail = head
    for i in range(len(T)):
        el = Node()
        el.val = T[i]
        tail.next = el
        tail = el
    return head.next


def printList(L):
    while L != None:
        print(L.val, end=" -> ")
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
        if L.val < pivot.val:
            tail_s.next = L
            tail_s = tail_s.next
        elif L.val == pivot.val:
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
    L, l = quicksort(L, l)
    return L, l


def SortH(p,k):
    head = p
    tail = p

    for _ in range(k + 1):
        tail = tail.next

    while tail != None:
        temp = tail.next
        tail.next = None
        head, tail = qsort(head)
        tail.next = temp
        head = head.next
        tail = tail.next

    return p

T = [2, 5, 3, 7, 13, 11, 17, 19, 29, 23, 31, 37, 43, 41, 47, 53, 59, 67, 61, 73, 71, 79, 83, 89]

L1 = tab2list(T)
L2 = tab2list(T)

start1 = timeit.default_timer()
L1 = SortH(L1, 10)
stop1 = timeit.default_timer()

start2 = timeit.default_timer()
L2, _ = qsort(L2)
stop2 = timeit.default_timer()

print(stop1 - start1)
print(stop2 - start2)