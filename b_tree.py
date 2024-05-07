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
    
    def split_child(self, x, i):
        pass
    
    def insert_non_full(self, x, k):
        pass

    def delete(self, k):
        # Implementar la eliminación de un valor en el B-Tree
        pass

    def search(self, k):
        # Implementar la búsqueda de un valor en el B-Tree
        pass

    def traverse(self):
        # Implementar el recorrido del B-Tree
        pass