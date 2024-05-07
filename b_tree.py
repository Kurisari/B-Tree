class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def insert(self, k):
        if len(self.root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode()
            new_root.child.append(self.root)
            self.root = new_root
            self.split_child(new_root, 0)
        self.insert_non_full(self.root, k)
    
    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(leaf=y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def delete(self, k):
        if not self.root.keys:
            return
        self.delete_key(self.root, k)
        if not self.root.keys:
            self.root = self.root.child[0]

    def delete_key(self, x, k):
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if i < len(x.keys) and k == x.keys[i]:
            if x.leaf:
                x.keys.pop(i)
            else:
                self.delete_internal_key(x, i)
        elif not x.leaf:
            self.delete_key_from_child(x, i, k)

    def delete_internal_key(self, x, i):
        if len(x.child[i].keys) >= self.t:
            predecessor = self.get_predecessor(x, i)
            x.keys[i] = predecessor
            self.delete_key(x.child[i], predecessor)
        elif len(x.child[i + 1].keys) >= self.t:
            successor = self.get_successor(x, i)
            x.keys[i] = successor
            self.delete_key(x.child[i + 1], successor)
        else:
            self.merge_children(x, i)

    def delete_key_from_child(self, x, i, k):
        if len(x.child[i].keys) == self.t - 1:
            if i > 0 and len(x.child[i - 1].keys) >= self.t:
                self.borrow_from_previous(x, i)
            elif i < len(x.child) - 1 and len(x.child[i + 1].keys) >= self.t:
                self.borrow_from_next(x, i)
            else:
                self.merge_children(x, i)
        self.delete_key(x.child[i], k)
    
    def get_predecessor(self, x, i):
        current = x.child[i]
        while not current.leaf:
            current = current.child[-1]
        return current.keys[-1]

    def get_successor(self, x, i):
        current = x.child[i + 1]
        while not current.leaf:
            current = current.child[0]
        return current.keys[0]

    def borrow_from_previous(self, x, i):
        child = x.child[i]
        sibling = x.child[i - 1]
        child.keys.insert(0, x.keys[i - 1])
        x.keys[i - 1] = sibling.keys.pop()
        if not child.leaf:
            child.child.insert(0, sibling.child.pop())

    def borrow_from_next(self, x, i):
        child = x.child[i]
        sibling = x.child[i + 1]
        child.keys.append(x.keys[i])
        x.keys[i] = sibling.keys.pop(0)
        if not child.leaf:
            child.child.append(sibling.child.pop(0))

    def merge_children(self, x, i):
        child = x.child[i]
        sibling = x.child[i + 1]
        child.keys.append(x.keys[i])
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.child.extend(sibling.child)
        x.keys.pop(i)
        x.child.pop(i + 1)

    def search(self, k):
        # Implementar la búsqueda de un valor en el B-Tree
        pass

    def traverse(self):
        # Implementar el recorrido del B-Tree
        pass