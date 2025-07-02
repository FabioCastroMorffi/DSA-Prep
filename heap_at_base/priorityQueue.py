from heapArray import Heap

class PriorityQueue:
    def __init__(self):
        self._pqueue = Heap()
    def  add(self, key, value):
        return self._pqueue.add(key,value)
    def min(self):
        return self._pqueue.min()
    def removeMin(self):
        return self._pqueue.removeMin()
    def isEmpty(self):
        return self._pqueue._size == 0
    def __len__(self):
        return len(self._pqueue)


if '__main__' == __name__:
    priority_queue = PriorityQueue()
    priority_queue.add(3, 'b')
    priority_queue.removeMin()
    print(priority_queue.isEmpty(), len(priority_queue))