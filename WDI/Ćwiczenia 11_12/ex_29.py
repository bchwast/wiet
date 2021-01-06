class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


class LL:
    def __init__(self, first=None):
        self.first = first

    def __str__(self):
        p = self.first
        if not p:
            return "pusto"
        ret = ""
        while p:
            ret += f"{p.val} -> "
            p = p.next
        return ret

    def insert(self, el):
        new_el = Node(el)
        if not self.first:
            self.first = new_el
            return

        p = None
        r = self.first
        while r:
            p = r
            r = r.next

        p.next = new_el
        return
#end class


def czy_jest(l1, el):
    if not l1.first:
        return 2
    first = l1.first

    if first.val > el:
        return 1
    if first.val == el:
        l1.first = l1.first.next
        return 0

    p = first
    r = first.next
    while r:
        if r.val > el:
            return 1
        if r.val == el:
            p.next = r.next
            del r
            return 0
        p = r
        r = r.next
    if el > p.val:
        return 2
    return 1
#end def


def powtorki(l1, l2):
    if not l2.first:
        return 0
    cnt = 0

    while czy_jest(l1, l2.first.val) == 0:
        l2.first = l2.first.next
        cnt += 1

    if not l2.first:
        return cnt

    p = l2.first
    r = l2.first.next
    while r:
        flaga = czy_jest(l1, r.val)
        if flaga == 0:
            p.next = r.next
            del r
            cnt += 1
            r = p.next
        elif flaga == 1:
            p = r
            r = r.next
        else:
            break
    #end while
    return cnt
#end def


l1 = LL()
l2 = LL()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(6)
l2.insert(2)
l2.insert(5)
l2.insert(6)
l2.insert(7)
print(l1,l2, sep="\n")
print(powtorki(l1,l2))
print(l1,l2, sep="\n")


