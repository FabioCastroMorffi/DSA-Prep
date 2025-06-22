#from empty.empty_exception import Empty

# Fixed Array Implementation

class QueueList:
    def __init__(self, size:int):
        self.__size = size
        self.__data = [None] * size
        self.__back = 0
        self.__front = 0
    
    def enqueue(self, value: object):
        if self.__back == self.__size:
            raise 'Max size'
        self.__back += 1 
        self.__data.append(value)
        
    def isEmpty(self):
        return (self.__back - self.__front) == 0
    def dequeue(self):
        if self.isEmpty():
            raise 'Container is empty'
        else:
            top = self.first()
            self.__data[self.__front] = None
            self.__front += 1
            return(top)
    def first(self):
        return( self.__data[self.__front])
    def __len__(self):
        return self.__back - self.__front
    
if '__main__' == __name__:
    queue = QueueList(3)
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.first())
    #print(queue.dequeue())
    queue.enqueue(2)
    print(queue.dequeue())
    print(len(queue))




