class CircularQueue:
    def __init__(self, maxsize):
        self._data = [0] * maxsize
        self._size = 0
        self._front = 0
        self._max = maxsize
    def isEmpty(self)->bool:
        return (self._size) == 0
    def first(self) -> object:
        if self.isEmpty():
            raise ('Empty')
        else:
            return (self._data[self._front])
    def enqueue(self,element:object):
        if self._size == self._max:
            raise 'Full'
        self._data[(self._size + self._front) % self._max] = element
        self._size += 1
    def dequeue(self):
        if self.isEmpty():
            raise 'Empty'
        else:
            top = self.first()
            self._data[self._front] = None
            self._size -= 1
            self._front = (self._front + 1) % self._max
            return top
    def __len__(self):
        return self._size
    def __repr__(self):
        if self.isEmpty():
            return '||'
        answer = '|'
        for elem in self._data:
            answer += str(elem) + '|'
        return answer
    
if '__main__' == __name__:
    cqueue = CircularQueue(4)
    print(cqueue)
    cqueue.enqueue(1)
    cqueue.enqueue('a')
    print(cqueue.dequeue())
    cqueue.enqueue(1)
    print(cqueue.first())
    print(len(cqueue))
    print(cqueue)
    cqueue.enqueue(9)
    print(cqueue)
    cqueue.dequeue()
    print(cqueue)

        


        
