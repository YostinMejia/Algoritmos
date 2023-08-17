# Throw an IllegalArgumentException if the client calls either 
# addFirst() or addLast() with a null argument.
class IllegalArgumentException(Exception):
    def __init__(self, message = " Null argument.") -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message
    
class NoSuchElementException(Exception):

    def __init__(self, message = "The deque is empty.") -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class UnsupportedOperationException(Exception):
    def __init__(self, message = "Can't call the remove() method in the iterator") -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message
