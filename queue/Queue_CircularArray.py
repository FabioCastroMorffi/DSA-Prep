class CircularQueue:
    def __init__(self, maxsize):
        self.__data = [None] * maxsize
        self.__size = 0
        self.__front = 0
        self.__max = maxsize
    def isEmpty(self)->bool:
        return (self.__size) == 0
    def first(self) -> object:
        if self.isEmpty():
            raise ('Empty')
        else:
            return (self.__data[self.__front])
    def enqueue(self,element:object):
        if self.__size == self.__max:
            raise 'Full'
        self.__data[(self.__size + self.__front) % self.__max] = element
        self.__size += 1
    def dequeue(self):
        if self.isEmpty():
            raise 'Empty'
        else:
            top = self.first()
            self.__data[self.__front] = None
            self.__size -= 1
            self.__front += 1
            return top
    def __len__(self):
        return self.__size
    
if '__main__' == __name__:
    cqueue = CircularQueue(3)
    cqueue.enqueue(1)
    cqueue.enqueue(2)
    print(cqueue.dequeue())
    cqueue.enqueue(1)
    print(cqueue.first())
    print(len(cqueue))


        


        
