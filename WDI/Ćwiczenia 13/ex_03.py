class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
#end class

def search(t, el):
    if t is None or t.val == el:
        return t
    if el < t.val:
        return search(t.left, el)
    return search(t.right, el)
#end def

