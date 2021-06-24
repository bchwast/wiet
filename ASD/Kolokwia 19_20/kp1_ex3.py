from kp1_ex3_testy import runtests

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.cnt = 1


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right


def switch(root, key):
    if root.key == key:
        root.cnt -= 1
        return root
    elif key < root.key:
        root.left = switch(root.left, key)
    else:
        root.right = switch(root.right, key)
    return root


def check(root, key):
    r = root
    while True:
        if root.key == key:
            if root.cnt > 0:
                root.cnt += 1
                return r, True
            root.cnt += 1
            return r, False
        elif key < root.key:
            if root.left is None:
                root.left = BSTNode(key)
                return r, False
            root = root.left
        else:
            if root.right is None:
                root.right = BSTNode(key)
                return r, False
            root = root.right



def longest_incomplete( A, k ):
    n = len(A)
    t = BSTNode(-1)

    m, curr, present = 0, 0, 0
    for i in range(n):
        print(i, A[i], curr)
        t, c = check(t, A[i])
        if not c:
            present += 1
            if present == k:
                for j in range(i - curr, i):
                    node = find(t, A[j])
                    if node.cnt == 1:
                        t = switch(t, A[j])
                        break
                    else:
                        t = switch(t, A[j])
                        curr -= 1
                        present -= 1
            else:
                curr += 1
                m = max(m, curr)
        else:
            curr += 1
            m = max(m, curr)




    return m


runtests( longest_incomplete ) 
