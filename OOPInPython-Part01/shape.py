'''
	OOPInPython-Part01
	https://levelup.gitconnected.com/oop-in-python-a-comprehensive-guide-to-key-terms-and-concepts-f19bcfd08dc6
'''

# Polymorphism -> Present the same interface for different data types.

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self): # Polymorphic method
        return (f'area of the circle is {3.14 * self.radius ** 2}')

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self): # Polymorphic method
        return (f'area of square is {self.side ** 2}')
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self): # Polymorphic method
        return (f'area of triangle is {.5 * self.base * self.height}')
    
shapes = [Circle(5), Square(5), Triangle(5, 5)]
for shape in shapes:
    print(shape.area())

# Output1:    area of the circle is 78.5
# Output2:    area of square is 25
# Output3:    area of triangle is 12.5