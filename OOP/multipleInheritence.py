# multiple inheritence = a child class can inherit from more than one parent class, it can be useful when you want to create a class that combines the functionality of multiple classes
class Animal:
    def eat(self):
        print("Eating...")

class Mammal():
    def walk(self):
        print("Walking...")
class Dog(Animal,Mammal):
    def bark(self):
        print("Barking...")

dog = Dog()
dog.eat()
dog.walk()  
dog.bark()


# multilevel inheritence = a child class can also be a parent class, it is a way to create a hierarchy of classes
class Animal:
    def eat(self):
        print("Eating...")
class Mammal(Animal):
    def walk(self):
        print("Walking...")
class Dog(Mammal):
    def bark(self):
        print("Barking...")

dog = Dog()
dog.eat()
dog.walk()
dog.bark()

