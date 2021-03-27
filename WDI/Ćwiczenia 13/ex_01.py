class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#end class

class Tree:
    def __init__(self, root=None):
        self.root = root
#end class

def wypisz(t):
    if t is not None:
        print(t.val)
        wypisz(t.left)
        wypisz(t.right)
#end def

def elementy(t, el=0):
    s = 1
    if t is not None:
        s += elementy(t.left, s)
        s += elementy(t.right, s)
        return s
    else:
        return 0
#end def

def wysokosc(t):
    if t is not None:
        l = wysokosc(t.left)
        r = wysokosc(t.right)
        h = max(l, r)
        return h + 1
    else:
        return 0
#end def

def liscie(t, l=0):
    s = 0
    if t is not None:
        if t.left is None and t.right is None:
            return 1
        s += liscie(t.left, s)
        s += liscie(t.right, s)
        return s
    else:
        return 0
#end def

def wezly(t, k, w=0):
    s = 0
    if t is not None:
        if k == 0 and not (t.left is None and t.right is None):
            return 1
        s += wezly(t.left, k-1, s)
        s += wezly(t.right, k-1, s)
        return s
    else:
        return 0
#end def

def wartosc(t, val):
    if t is not None:
        if t.val == val:
            return True
        return wartosc(t.left, val) or wartosc(t.right, val)

    return False
#end def

def usun(t, d=False):
    if t is None:
        return t

    usun(t.left)
    usun(t.right)

    t = None
#end def

def trim(t, k):
    if k == 0:
        if t is None:
            return

        trim(t.left, k)
        trim(t.right, k)

        t = None
        return t
    else:
        if t is not None:
            t.left = trim(t.left, k-1)
            t.right = trim(t.right, k-1)

        return t
#end def

tree = Node(3)
tree.left = Node(5)
tree.right = Node(7)
tree.left.left = Node(2)
tree.right.left = Node(9)
tree.right.right = Node(11)
tree.right.right.right = Node(13)
print(wysokosc(tree))
tree = trim(tree, 2)
print(wysokosc(tree))
