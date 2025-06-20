#from empty.empty_exception import Empty

# Fixed Array Implementation

class Queue:
    def __init__(self, size:int):
        self.__size = size
        self.__data = [] * size
        self.__back = 0
        self.__front = 0
    
    def enqueue(self, value: object):
        self.__back += 1
        if self.__back > self.__size:
            raise 'Max size' 
        self.__data.append(value)
        
    def isEmpty(self):
        return (self.__back - self.__front) == 0
    def dequeue(self):
        if self.isEmpty():
            raise 'Container is empty'
        else:
            self.__data[self.__front] = None
            self.__front += 1
            return(self.__data[self.__front])
    def first(self):
        print( self.__data[self.__front])
    def __len__(self):
        return self.__back - self.__front
    
if '__main__' == __name__:
    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.first()
    #print(queue.dequeue())
    queue.enqueue(2)
    queue.enqueue(2)




