# parent class
class Pets:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display_details(self):
        print(f"\n Name: {self.name}\n Age: {self.age}")
    
class Dog(Pets):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} barks.")

class Cat(Pets):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed
    def speak(self):
        print(f"{self.name} the {self.breed} Meows.")

dog = Dog("Bbhotey",breed="Golden Retriever",age= 5)
cat = Cat("Kaley",2,breed=" Persian")

cat.display_details()
cat.speak()

dog.display_details()
dog.speak()