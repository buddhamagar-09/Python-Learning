# statics and instance methods
# static = a methods that belongs to the class rather than an object of the class and uses decorator @staticmethod
# instance = a method that belongs to the object of the class rather than the class itself
class Demo :
    def __init__(self,sname,position):
        self.sname = sname
        self.position = position

    def get_info(self):
        print(f"{self.sname} = {self.position}")
    
    @staticmethod
    def is_validposition(position):
        positions = ["Manager","IT Head","CEO"]
        return position in positions
    
d = Demo("buddha","Manager")
d.get_info()

print(Demo.is_validposition("Manager"))


# another Example
# Instance variables: name and marks

# Instance method display() that prints student details

# Static method is_pass(marks)

# returns "Pass" if marks ≥ 40

# otherwise "Fail"


class Result:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        return f"Name: {self.name}\n Marks: {self.marks}"

    @staticmethod
    def is_pass(marks):
        return "pass" if marks >= 40 else "fail"
    
res = [ Result("Buddha", 99),
        Result("Pawan", 88),
        Result("Sushant", 91),
        Result("Hero", 44)
        ]

for result in res:
    print(result.display())
    print(f"Result: ",Result.is_pass(result.marks))