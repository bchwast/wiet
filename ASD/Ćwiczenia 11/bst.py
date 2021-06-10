class BSTNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f"[{self.key} : {self.val}]"

    def __repr__(self):
        return f"[{self.key} : {self.val}]"


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def insert(root, key, value):
    prev = None
    side = None
    while root is not None:
        if root.key == key:
            return False
        prev = root
        if key < root.key:
            root = root.left
            side = 0
        else:
            root = root.right
            side = 1
    node = BSTNode(key, value)
    node.parent = prev
    if side == 0:
        prev.left = node
    else:
        prev.right = node
    return True


def min_node(root):
    prev = None
    while root is not None:
        prev = root
        root = root.left
    return prev


def max_node(root):
    prev = None
    while root is not None:
        prev = root
        root = root.right
    return prev


def succ(root, key=None):
    if key is not None:
        root = find(root, key)
    if root.right is not None:
        return min_node(root.right)
    prev = root.parent
    while prev is not None and prev.right == root:
        root = prev
        prev = root.parent
    return prev


def pred(root, key=None):
    if key is not None:
        root = find(root, key)
    if root.left is not None:
        return max_node(root.left)
    prev = root.parent
    while prev is not None and prev.left == root:
        root = prev
        prev = root.parent
    return prev


# def delete(root, key):
#     dead = find(root, key)
#     if dead is None:
#         return False
#
#     if dead.left is None and dead.right is None:
#         if dead.parent is None:
#             root = None
#             return True
#         if dead.parent.right == dead:
#             dead.parent.right = None
#         elif dead.parent.left == dead:
#             dead.parent.left = None
#         dead = None
#         return True


tree = BSTNode(20, 1)
T = [3, 4, 23, 5, 76, 42, 6, 32, 69, 234, 45, 22]
for i in range(len(T)):
    insert(tree, T[i], 1)
print(succ(pred(max_node(tree))))

