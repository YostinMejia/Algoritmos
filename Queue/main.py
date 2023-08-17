from deque import LinkedListDeque, CircularArrayDeque

linkedList = LinkedListDeque()
circularArray = CircularArrayDeque(5)

for i in range(1,8):
    linkedList.addLast(i+1)
    linkedList.addFirst(i+10) 
    circularArray.addLast(i+1)
    circularArray.addLast(i+1)


linkedList.removeLast()
linkedList.removeFirst()
circularArray.removeLast()
circularArray.removeFirst()

iteradorList = linkedList.iterator()
iteradorArray = linkedList.iterator()
circularArray.display()
while iteradorList.hasNext() :
    print(iteradorList.next())
    print(iteradorArray.next())
