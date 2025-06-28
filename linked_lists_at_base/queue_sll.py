#from empty import Empty

class LinkedQueue:
    '''Fifo queue implementation using a sll'''

    #---------> nest Node class------------
    class _Node:
        '''lightweight non-public class for storing sll'''
        __slots__ = '_element', '_next' #class attributes

        def __init__(self,element, next):
            '''create a Node'''
            self._element = element
            self._next = next
    #--------------------------------------

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def first(self):
        if self.isEmpty():
            raise ('Queue is empty')
        
        return self._head._element
    
    def dequeue(self):
        if self.isEmpty():
            raise ('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isEmpty(): # removed head had been tail
            self._tail = None
        return answer
    
    def enqueue(self,elem):
        new_node = self._Node(elem, None)
        if self.isEmpty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

if '__main__' == __name__:
    ll = LinkedQueue()
    ll.enqueue(3)
    ll.enqueue(4)
    print(ll.first())
    


