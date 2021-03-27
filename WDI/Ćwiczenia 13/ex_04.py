class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
#end class

def insert(t, key):
    if t is None:
        return Node(key)

    if t.val == key:
        return t
    elif key < t.val:
        t.left = insert(t.left, key)
    else:
        t.right = insert(t.right, key)

    return t
#end def
