class SinglyLinkedList:
    class _Node:
        ___slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size == 0
    def insertAtHead(self, elem):
        new_node = self._Node(elem, self._head)
        if self.isEmpty():
            self._tail = new_node
        self._head = new_node
        self._size += 1
    def insertAtTail(self, elem):
        new_node = self._Node(elem, None)
        if self.isEmpty():
            self._head = new_node
        self._tail = new_node
        self._size += 1
    def addAtIndex(self, index, elem):
        if index < self.__len__():
            prev = self._head
            for i in range(index-1):
                prev = prev._next
            new_node = self._Node(elem, prev)
        if index == self.__len__():
            self.insertAtTail(elem)