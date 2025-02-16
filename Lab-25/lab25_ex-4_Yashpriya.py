# Part-A
class Quadrilateral:
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
    def isSquare(self):
        return self.side1 == self.side2 == self.side3 == self.side4
    def isRectangle(self):
        return self.side1 == self.side3 and self.side2 == self.side4 and self.side1 != self.side2

# Instance-a (All the sides being different)
q = Quadrilateral(2, 4, 5, 6)
print(f"Quadrilateral is a square (All the sides being different): {q.isSquare()}")
print(f"Quadrilateral is a rectangle (All the sides being different): {q.isRectangle()}")

# Instance-b (Opposite sides being different)
q1 = Quadrilateral(2, 2, 4, 4)
print(f"It is a square (Opposite sides being different): {q1.isSquare()}")
print(f"It is a rectangle (Opposite sides being different): {q1.isRectangle()}")

# Instance-c (All the sides being the same)
q2 = Quadrilateral(2, 2, 2, 2)
print(f"Quadrilateral is a square (All the sides being the same): {q2.isSquare()}")
print(f"Quadrilateral is a rectangle (All the sides being the same): {q2.isRectangle()}")


# Part-B (Inheritance)
class Square(Quadrilateral):
    def __init__(self, side1):
        super().__init__(side1, side1, side1, side1)   # Calling the parent's constructor
    def get_Sq_Area(self):
        return self.side1 * self.side1
class Rectangle(Quadrilateral):
    def __init__(self, side1, side2):
        super().__init__(side1, side2, side1, side2)
    def get_Rect_Area(self):
        return self.side1 * self.side2
square = Square(5)
print(f"Area of Square: {square.get_Sq_Area()}")
rectangle = Rectangle(4, 6)
print(f"Area of Rectangle: {rectangle.get_Rect_Area()}")






