from dll import DLL

class DeqDLL:
    def __init__(self):
        self._dll = DLL()
    def insertAtEnd(self, elem):
        self._dll.insertBetween(elem, self._dll.get(len(self._dll)-1), None)
    def insertAtStart(self, elem):
        self._dll.insertBetween(elem, None, self._dll.get(0))
    def removeAtEnd(self):
        if len(self._dll) != 0:
            self._dll.deleteNode(self._dll.get(len(self._dll)-1))
        else:
            raise 'Empty container'
    def removeAtStart(self):
        if len(self._dll) != 0:
            self._dll.deleteNode(self._dll.get(0))
        else:
            raise 'EMpty container'
    def __repr__(self):
        return self._dll.__repr__()

if __name__ == '__main__':
    deq = DeqDLL()
    deq.insertAtEnd(2)
    deq.insertAtEnd(3)
    deq.insertAtEnd(4)
    print(deq)
    deq.removeAtEnd()
    deq.removeAtStart() 
    print(deq)
    deq.removeAtStart()
    #deq.removeAtStart()
    print(deq)
        