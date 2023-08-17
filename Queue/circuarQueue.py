class CircularQueue:
    def __init__(self, N) -> None:
        self.queue = [None for _ in range (N)]
        self.N = N
        # posiciones 
        self.front = -1
        self.rear = -1
    
    def isEmpty(self):
        return self.front == self.rear == -1
    
    def isFull ( self):
        return (self.rear+1)%self.N == self.front
    
    def enqueue(self, item)->None:
        if self.isEmpty():
            self.front = (self.front+1)% self.N
            self.rear = (self.rear+1)% self.N
            self.queue[self.rear] = item
        elif self.isFull():
            print ("Is full")
        else:
            self.rear = (self.rear+1)%self.N
            self.queue[self.rear] = item
    
    def dequeue(self)->object:
        if self.isEmpty():
            print("Is empty")
        # Si es el ultimo elemento
        elif self.rear == self.front:
            item =  self.queue[self.front]
            self.queue[self.front] = None
            self.rear = -1
            self.front = -1
        else:
            item = self.queue[self.front] 
            self.queue[self.front] = None
            self.front = (self.front+1)%self.N
        return item
