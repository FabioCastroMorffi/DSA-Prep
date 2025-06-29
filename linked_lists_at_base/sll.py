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
        if index == self.__len__():
            self.insertAtTail(elem)
            self._size += 1
        elif index == 0:
            self.insertAtFront(elem)
            self._size += 1
        elif index < self.__len__():
            prev = self._head
            for i in range(index-1):
                prev = prev._next
            new_node = self._Node(elem, prev._next)
            prev._next = new_node
            self._size += 1
    def removeAtIndex(self, index):
        if index == 0 and not self.isEmpty():
            self._head = self._head._next
            self._size -= 1
        elif index == self.__len__() - 1:
            curr_node = self._head
            for i in range(index-1):
                curr_node = curr_node._next
            self._tail = curr_node
            curr_node._next = None
            self._size -= 1
        elif index < self.__len__() -1:
            curr_node = self._head
            prev = None
            for i in range(index):
                prev = curr_node
                curr_node = curr_node._next
            prev._next= curr_node._next
            self._size -= 1
    def __repr__(self):
        curr_node = self._head 
        lst = []
        for _ in range(self.__len__()):
            lst.append(str(curr_node._element))
            curr_node = curr_node._next
        return ' --> '.join(lst)
    def get(self, index):
        curr_node = self._head
        if 0<=index<self.__len__():
            for i in range(index):
                curr_node = curr_node._next
            return curr_node._element
        
if '__main__' == __name__:
    ll = SinglyLinkedList()
    ll.insertAtTail(3)
    ll.insertAtHead(2)
    ll.addAtIndex(1, 9)
    print(ll)
    ll.removeAtIndex(1)
    print(ll)
    print(ll.get(1))
    print(len(ll))

            
    
                


