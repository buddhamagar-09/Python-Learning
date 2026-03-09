# polymorphism = the ability to take many forms
# it can be achieved through method overriding and method overloading
# duck typing = concept of dynamic typing in python and its type is determined at runtime rather than compile time


from abc import ABC, abstractmethod

class Shapes:
    def area(self):
        pass

class Circle(Shapes):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * 2

class Square(Shapes):
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length * self.length

class Perimeter(Shapes):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
class Pizza(Circle):
    def __init__(self,radius):
        super().__init__(radius)

shapes = [Circle(4),Square(5),Perimeter(4,6),Pizza(4)]

for shape in shapes:
    print(f"{shape.area()}")
        