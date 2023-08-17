class IllegalArgumentException(Exception):
    def __init__(self, message = " Null argument.") -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message