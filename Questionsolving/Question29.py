# Shape Class with Circle and Square

class Shape:
    pass

class Circle(Shape):

    def area(self, r):
        return 3.14 * r * r

    def perimeter(self, r):
        return 2 * 3.14 * r

class Square(Shape):

    def area(self, s):
        return s * s

    def perimeter(self, s):
        return 4 * s

c = Circle()

print(c.area(5))
print(c.perimeter(5))

s = Square()

print(s.area(4))
print(s.perimeter(4))