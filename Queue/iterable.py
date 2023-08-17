from exception import NoSuchElementException, UnsupportedOperationException
     
# class Iterable:

#     def  __init__(self, first) -> None:
#         iterator = Iterator(first)

# class Iterator:
#     def __init__(self, first) -> None:
#         iterator = linkedListIterator(first)

class CircularArrayIterator():
    def __init__(self, front, size, array) -> None:
        self.current = front
        self.size = size 
        self.N
        self.N = len(array)
        
    def hasNext(self):
        return self.size >=0
    
    def next(self):
        if self.hasNext():
            raise NoSuchElementException("There are no more items to return.")
        
        item = self.current
        self.current = self
        return item
    
    def remove():
        raise UnsupportedOperationException("Client can't calls the remove() method in the iterator.")



class linkedListIterator():
    def __init__(self, front) -> None:
        self.current = front
        
    def hasNext(self):
        return self.current !=None
    
    def next(self):
        if not self.hasNext():
            raise NoSuchElementException("There are no more items to return.")
        
        item = self.current.item
        self.current = self.current.next
        return item
    
    def remove():
        raise UnsupportedOperationException("Client can't calls the remove() method in the iterator.")
