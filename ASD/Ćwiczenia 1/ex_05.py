class Node:
    def __init__(self):
        self.value = None
        self.next = None


def printList(L):
    while L != None:
        print(L.value, end = " -> ")
        L = L.next
    print()


def reverseList(L):
    if L.next is None:
        return L

    L = L.next
    prev = None
    nxt = L.next

    while L:
        L.next = prev
        prev = L
        L = nxt
        if nxt != None:
            nxt = nxt.next

    head = Node()
    head.next = prev

    return head


L = Node()
a = Node()
b = Node()
c = Node()
d = Node()
a.value = 5
b.value = 1
c.value = 13
d.value = 3
L.next = a
a.next = b
b.next = c
c.next = d
printList(L)
L = reverseList(L)
printList(L)