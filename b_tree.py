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
        pass

    def search(self, k):
        # Implementar la búsqueda de un valor en el B-Tree
        pass

    def traverse(self):
        # Implementar el recorrido del B-Tree
        pass