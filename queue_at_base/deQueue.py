from Queue_CircularArray import CircularQueue
class DeQueue:
    def __init__(self,max):
        self.__cqueue = CircularQueue(max)
    def insertFront(self,elem):
        pass
    def insertBack(self,elem):
        if len(self.__cqueue) == max:
            raise 'Container Full'
        self.__cqueue.enqueue(elem)
    def deleteFront(self):
        self.__cqueue.dequeue()
    
    
