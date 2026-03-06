# object = a real world entity that has some characteristics and behaviors
# you need a class to create an object

# class = a blueprint for creating objects. It defines a set of attributes that will characterize any object that is instantiated from the class

class Animal:
# class variable
    legs = 4
    # constrictor
    def __init__(self,name,type):
        # instance Variable
        self.name = name
        self.type = type
    
    def display_details(self):
        print(f"\rName: {self.name}\n Type: {self.type} \n Legs: {self.type}",flush=True,end="")

animal1 = Animal("Tiger","Carnivore")
animal1.display_details()



