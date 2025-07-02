import math
class Heap:
    def __init__(self):
        self._size = 0
        self._data = [] #tuples -> (key, value)
    def parent(self, index)-> int: # returns index
        return math.floor((index-1)/2) if index > 0 else None
    def left(self, index): #returns index
        return 2*index + 1 if  2*index + 1 < self._size else None
    def right(self, index): #returns index
        return 2*index + 2 if 2*index + 2 < self._size else None

    def has_right(self, index)-> bool: 
        return True if 2*index + 2 < self._size else False
    def has_left(self, index):
        return True if  2*index + 1 < self._size else False
    def swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def upheap(self, index): # logic operation depends on  
        while index != 0 and (self._data[index][0]  < self._data[self.parent(index)][0]):
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def downheap(self, index):
        while self.left(index) != None:
            if self.right(index) != None and self._data[self.left(index)][0] <= self._data[self.right(index)][0]:
                self.swap(index, 2*index+1)
                index = index * 2 + 1
            elif self.right(index) != None and self._data[self.right(index)][0] < self._data[self.left(index)][0]:
                self.swap(index, 2*index + 2)
                index = index *2 +2
            else:
                #print(self._data[index][0], self._data[self.left(index)][0])
                if self._data[index][0] > self._data[self.left(index)][0]:
                    self.swap(index, 2*index + 1)
                break
                


    
    def __repr__(self):
        return ' '.join(list(map(str, self._data)))
    def  __len__(self):
        return self._size
    def add(self, key, value):
        self._data.append((key, value))
        self._size += 1
        self.upheap(self._size - 1)
    def min(self):
        if self._size > 0:
            return self._data[0]
        else:
            raise 'Empty container'
    def removeMin(self):
        if self._size > 0:
            self.swap(0, self._size - 1)
            self._data.pop(self._size -1)
            self._size -=1
            self.downheap(0)
        else:
            raise 'Empty container'

        
if '__main__' == __name__:
    heap = Heap()
    heap.add(3,'a')
    heap.add(2, 'b')
    #print(heap)
    heap.add(7, 'c')
    heap.add(4,'d')
    heap.add(2,'e')
    heap.removeMin()
    print(heap)
    heap.removeMin()
    heap.removeMin()
    print(len(heap))
    print(heap)




        