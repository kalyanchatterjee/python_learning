class Point:
    # Class level attribute
    # Shared by all objects of this class
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()

another = Point(3, 4)
another.draw()
