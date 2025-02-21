class Rectangle:
    def _init_(self, length: int, width: int):
        self.length = length
        self.width = width

    def _iter_(self):
        yield {"length": self.length}
        yield {"width": self.width}


# Example usage
rect = Rectangle(10, 5)
for item in rect:
    print(item)