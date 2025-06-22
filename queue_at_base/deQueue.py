from Queue_CircularArray import CircularQueue

## Main takeaway(cause i spent too much time on this):
## - In order to advance in a modular manner, it was just front = (front + 1) % max ; whenever one goes over max we go back 
## - A circular queue is necessary for this cause the pointers to the front and back of the queue change with deletion and insertion, but grosso modo
##   a queue that goes from 2 to 4 and one that goes from 4 to 1 is the same, nothing changes except the pointers

class DeQueue:
    def __init__(self,max):
        self.__cqueue = CircularQueue(max)

    def insertRight(self,elem):
        return self.__cqueue.enqueue(elem)
    def __len__(self):
        return self.__cqueue._size
    def insertLeft(self,elem):
        if len(self.__cqueue) == self.__cqueue._max:
            raise 'Full array'
        self.__cqueue._front = (self.__cqueue._front -1) % self.__cqueue._max
        self.__cqueue._data[self.__cqueue._front] = elem
        self.__cqueue._size += 1
    def deleteLast(self):
        if not len(self.__cqueue):
            raise 'Empty Container'
        return_index = (self.__cqueue._front + self.__cqueue._size-1) % self.__cqueue._max
        return_value = self.__cqueue._data[return_index]
        self.__cqueue._data[return_index] = None
        self.__cqueue._size -= 1    
        return return_value

    def deleteFirst(self):
        return self.__cqueue.dequeue()
    def first(self):
        return self.__cqueue.first()
    def last(self):
        if not len(self.__cqueue):
            raise 'Empty Container'
        return self.__cqueue._data[(self.__cqueue._front + self.__cqueue._size-1) % self.__cqueue._max]

if '__main__' == __name__:
    a = DeQueue(3)
    a.insertLeft(2)
    a.insertRight(3)
    #print(a._size)
    print(len(a))
    a.insertLeft(3)
    a.insertLeft('a')
    print(a.first())
    
        
        
    
    
