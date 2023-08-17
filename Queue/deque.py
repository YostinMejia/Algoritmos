
"""Performance requirements. 
Your deque implementation must support each deque operation (including construction) 
in constant worst-case time. 
A deque containing n items must use at most 48n + 192 bytes of memory. 
Additionally, your iterator implementation must support each operation 
(including construction) in constant worst-case time."""
from iterable import linkedListIterator, CircularArrayIterator
from exception import IllegalArgumentException, NoSuchElementException

class Node:

    def  __init__(self, item, next, prev) -> None:
        self.item = item
        self.next = next
        self.prev = prev

class Deque():

    def __init__(self) -> None:
        """self._size =0
        self.front = None
        self.rear = None"""

    def isEmpty(self)->bool:
        """ Is the deque empty?"""
    
    def size(self)->int:
        """ return the number of items on the deque"""
    
    def addFirst(self, item:object)->None:
        """#  add the item to the front"""
  

    def addLast (self, item:object)->None:
        """# add the item to the rear"""


    def removeFirst(self)->object:
        """# remove and return the intem from the front"""


    def removeLast(self)->object:
        """# remove and return the intem from the rear"""

    def iterator(self)->linkedListIterator:
       """ # return an iterator over items in order from front to rear"""


class LinkedListDeque(Deque):

    def __init__(self) -> None:
        self._size =0
        # se almacenan los nodos
        self.front = None
        self.rear = None

    def isEmpty(self)->bool:
        return self.front == None
    
    def size(self)->int:
        return self._size
    
    def addFirst(self, item:object)->None:
        if item == None:
            raise IllegalArgumentException
        
        first = self.front
        new = Node(item, first,None)
        if self.isEmpty():
            self.rear = new 
        else:
            first.prev = new
            new.next = first

        self.front = new
        self._size+=1

    def addLast (self, item:object)->None:
        if item == None:
            raise IllegalArgumentException
        
        last = self.rear
        new =  Node(item, None,last)
        if self.isEmpty():
            self.front = new 
        else:
            last.next = new
            new.prev = last
        self.rear = new
        self._size+=1
            
    def removeFirst(self)->object:
        if self.isEmpty():
            raise NoSuchElementException
        
        first = self.front
        self.front = first.next
        self.front.prev = None
        first.next = None
        self._size-=1
        return first.item

    def removeLast(self)->object:
        if self.isEmpty():
            raise NoSuchElementException
        
        last = self.rear
        self.rear = last.prev
        self.rear.next = None
        last.prev = None
        self._size-=1
        return last.item
        
    def iterator(self)->linkedListIterator:
        listIterator = linkedListIterator(self.front)
        return listIterator


class CircularArrayDeque(Deque):

    def __init__(self, N) -> None:
        self.queue = [None for _ in range (N)]
        self._size = 0
        self.N = N
        # posiciones 
        self.front = -1
        self.rear = -1
    
    def isEmpty(self):
        return self.front == self.rear == -1
    
    def isFull ( self):
        return (self.rear+1)%self.N == self.front
    
    def size(self)->int:
        return self._size
    
    def addFirst(self, item:object)->None:
        if item == None:
            raise IllegalArgumentException
        
        if self.isEmpty():
            self.front = (self.front+1)% self.N
            self.rear = (self.rear+1)% self.N
            self.queue[self.rear] = item
            self._size+=1
        elif self.isFull():
            print ("Is full")
        else:
            self.front = (self.front-1)%self.N
            self.queue[self.front] = item
            self._size+=1

    def addLast (self, item:object)->None:
        if item == None:
            raise IllegalArgumentException
        
        if self.isEmpty():
            self.front = (self.front+1)% self.N
            self.rear = (self.rear+1)% self.N
            self.queue[self.rear] = item
            self._size+=1
        elif self.isFull():
            print ("Is full")
        else:
            self.rear = (self.rear+1)%self.N
            self.queue[self.rear] = item
            self._size+=1
            
    def removeFirst(self)->object:
        if self.isEmpty():
            raise NoSuchElementException
        
        # Si es el ultimo elemento
        if self.rear == self.front:
            item =  self.queue[self.front]
            self.queue[self.front] = None
            self.rear = -1
            self.front = -1
        else:
            item = self.queue[self.front] 
            self.queue[self.front] = None
            self.front = (self.front+1)%self.N
        self._size -=1
        return item
            
    def removeLast(self)->object:
        if self.isEmpty():
            raise NoSuchElementException
        
        # Si es el ultimo elemento
        if self.rear == self.front:
            item =  self.queue[self.front]
            self.queue[self.front] = None
            self.rear = -1
            self.front = -1
        else:
            item = self.queue[self.rear] 
            self.queue[self.rear] = None
            self.rear = (self.rear-1)%self.N
        return item
        
    def display(self)->None:
        print(self.queue)
        # position = self.front
        # while position != self.rear:
        #     print(self.queue[position])
        #     position = (position+1)%self.N
        # print(self.queue[position])


            
