#from empty.empty_exception import Empty
class Stack:
    def __init__(self):
        self.__data = []
    def push(self, value):
        self.__data.append(value)
    def isEmpty(self):
        return not(len(self.__data))
    def pop(self):
        if self.isEmpty():
            raise ("Empty container")
        else:
            val = self.__data.pop(-1)
            return val
    def __len__(self):
        return len(self.__data)
    
    def top(self):
        if self.isEmpty():
            raise ("Empty container")
        return self.__data[-1]
    
    

if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.push('a')
    stack.pop()
    stack.pop()
    print(stack.isEmpty())
    print(len(stack))
    stack.top()


        
