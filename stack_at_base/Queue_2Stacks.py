from Stack_ADT import Stack

# main takeaway: u dont need to return the stuff from the hanoi stack to the main, its if hanoi not empty: pop, else: stuff from main to hanoi (no need for anything else)
class QueueStacks:
    def __init__(self):
        self.__main = Stack()
        self.__hanoi = Stack()
    def __len__(self):
        return len(self.__main)
    def isEmpty(self):
        return not len(self.__main)
    def enqueue(self,elem):
        self.__main.push(elem)
    def dequeue(self):
        if not self.__hanoi.isEmpty():
            return self.__hanoi.pop()
        else:
            if self.__main.isEmpty():
                raise 'Empty container'
            else:
                for i in range(len(self.__main)):
                    self.__hanoi.push(self.__main.pop())
                return self.__hanoi.pop()
    def first(self):
        if not self.__hanoi.isEmpty():
            return self.__hanoi.top()
        else:
            if self.__main.isEmpty():
                raise 'Empty container'
            else:
                for i in range(len(self.__main)):
                    self.__hanoi.push(self.__main.pop())
                return self.__hanoi.top()
            

if '__main__' == __name__:
    q = QueueStacks()
    q.enqueue(3)
    q.enqueue(6)
    print(q.dequeue())
    print(q.dequeue())
    q.dequeue()




