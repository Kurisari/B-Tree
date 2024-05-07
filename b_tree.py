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
        # Implementar la inserción de un valor en el B-Tree
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