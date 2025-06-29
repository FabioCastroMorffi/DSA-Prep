class DLL:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, elem, prev, next):
            self._element = elem
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def insertBetween(self, elem: object, predecessor: _Node, successor: _Node):
        new_node = self._Node(elem, predecessor, successor)
        if predecessor == successor == None:
            self._header = new_node
            self._trailer = new_node
        elif predecessor == None:
            successor._prev = new_node
            self._header = new_node
        elif successor == None:
            predecessor._next = new_node
            self._trailer = new_node
        else:
            predecessor._next = new_node
            successor._prev = new_node
        self._size += 1
            
        
    
    def deleteNode(self, node):
        if node == self._header and node != self._trailer:
            next_node = self._header._next
            next_node._prev = None
            self._header = next_node 
        elif node == self._trailer and node != self._header:
            prev_node = self._trailer._prev
            next_node._next = None
            self._trailer = prev_node
        elif self.__len__() == 1:
            self._header = self._trailer = None
        else:
            predecessor = node._prev
            successor = node._next
            successor._prev = predecessor
            predecessor._next = successor
        self._size -= 1
    def get(self, index) -> _Node:
        curr_node = self._header
        if 0<=index<self.__len__():
            for i in range(index):
                curr_node = curr_node._next
            return curr_node
    def __repr__(self):
        curr_node = self._header 
        lst = []
        for _ in range(self.__len__()):
            lst.append(str(curr_node._element))
            curr_node = curr_node._next
        return ' --> '.join(lst)
    
if '__main__' == __name__:
    dll = DLL()
    dll.insertBetween(3, None, None)
    dll.insertBetween(9, dll.get(0), None)
    dll.insertBetween(10, dll.get(0), dll.get(1))
    dll.deleteNode(dll.get(0))
    print(dll)

            
            
            
    
            