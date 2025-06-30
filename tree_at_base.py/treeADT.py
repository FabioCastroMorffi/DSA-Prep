from collections import deque
class Tree:
    class _Node:
        def __init__(self, elem, parent=None, right=None, left=None):
            self._elem = elem
            self._right = right
            self._left = left
            self._parent = parent
    def __init__(self):
        self._root = None
        self._size = 0
    def root(self):
        return self._root
    def isRoot(self, node):
        return node == self._root
    def parent(self, node):
        if node == self._root:
            return None
        else:
            return node._parent._elem
    def children(self, node):
        return [node._left._elem, node._right._elem]
    def isLeaf(node):
        return node._left == node._right == None
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size == 0
    
    def depthKnode(self, node):
        count = 0
        while node != self._root:
            node = node._parent
            count += 1
        return count
    def heightKnode(self, node):
        count = 0
        if self.isLeaf(node):
            return count
        
        ## BFS ##

        queue = deque()
        if self._root:
            queue.append(self._root)

        while queue:
            for i in range(len(queue)):
                curr_node = queue.pop()
                if curr_node._left:
                    queue.append(curr_node._left)
                if curr_node._right:
                    queue.append(curr_node._right)
            count += 1
        return count -1 

    def __repr__(self):
        lst = []
        queue = deque()
        if self._root:
            queue.append(self._root)

        while queue:
            for i in range(len(queue)):
                curr_node = queue.pop()
                lst.append(curr_node._elem)
                if curr_node._left:
                    queue.append(curr_node._left)
                if curr_node._right:
                    queue.append(curr_node._right)
        return ' '.join(list(map(str, lst)))






                


          