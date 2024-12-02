class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return int(3.14 * self.radius ** 2 * 100) / 100

    def perimeter(self):
        return int(2 * 3.14 * self.radius * 100) / 100

class Rectangle(Shape):
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a=1, b=1, c=1):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return "Invalid triangle."

        s = (self.a + self.b + self.c) / 2
        return int((s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5 * 100) / 100

    def perimeter(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return "Invalid triangle."

        return self.a + self.b + self.c

rectangle = Rectangle(2, 3)
circle = Circle(5)
triangle = Triangle(3, 4, 5)

print("Rectangle : ")
print("Area : " + str(rectangle.area()))
print("Perimeter : " + str(rectangle.perimeter()))

print("\nCircle : ")
print("Area : " + str(circle.area()))
print("Perimeter : " + str(circle.perimeter()))

print("\nTriangle : ")
print("Area : " + str(triangle.area()))
print("Perimeter : " + str(triangle.perimeter()))

