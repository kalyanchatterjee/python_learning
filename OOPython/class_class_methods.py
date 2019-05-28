class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)
        # During runtime, the above passes a reference to the Point class
        # and calls the class constructor (__init__)

    def draw(self):
        print(f"Point is ({self.x}, {self.y})")


# Call the classmethod
point = Point.zero()
point.draw()
