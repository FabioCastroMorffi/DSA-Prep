from treeADT import Tree
class BinaryTree(Tree):
    def left(self, node):
        return node._left
    def right(self, node):
        return node._right
    def sibling(self, node):
        if node._parent._right == node:
            return node._parent._left
        else:
            return node._parent._right
    def addRoot(self, elem):
        new_node = super()._Node(elem, None, None, None)
        self._root = new_node
        self._size += 1
    def addLeft(self, node, elem):
        node._left = super()._Node(elem, node, None, None)
    def addRight(self, node, elem):
        node._right = super()._Node(elem, node)
    def replace(self, node, elem):
        node._elem = elem
    def delete(self, node):
        if node._left and node._right:
            raise 'Two child error'
        elif not(node._left and node._right):
            if node._parent.right() == node:
                node._parent._right = None
            else:
                node._parent._left = None
        elif node._left:
            if node._parent._right == node:
                node._parent._right = node._left
            else:
                node._parent._left = node._left
        else:
            if node._parent._right == node:
                node._parent._right = node._right
            else:
                node._parent._left = node._right
    def attach(self, node, T1: Tree, T2: Tree):
        if node.isLeaf():
            node._left = T1.root()
            node._right = T2.root()
    def __repr__(self):
        return super().__repr__()

if '__main__' == __name__:
    bt = BinaryTree()
    bt.addRoot(3)
    bt.addRight(bt.root(), 5)
    bt.addLeft(bt.root(), 4)
    bt.addRight(bt.root(),6)
    bt.children(bt.root())
    print(bt)


            
