import math

class Shape:
    def __init__(self):
        self.color = (1,2,3)

class Rectangle(Shape):
    def __init__(self, w, h):
        Shape.__init__(self)
        self.width = w
        self.height = h

    def area(self):
        return self.width*self.height

class Circle(Shape):
    def __init__(self, rad):
        Shape.__init__(self)
        self.radius = rad
    def area(self):
        return math.pi*(self.radius**2)

l = []
l.append( Rectangle(4,5) )
l.append( Circle(3) )
for someshape in l:
    print (someshape.area())
