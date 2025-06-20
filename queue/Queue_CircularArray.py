class Queue:
    def __inti__(self, size):
        self.__size = size
        self.__front = 0
        self.__back = 0
    def isEmpty(self):
        return self.__back - self.__front