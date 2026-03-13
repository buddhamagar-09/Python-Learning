# class methods =  a methods that belongs to class rather than an object of the class and uses decorator @classmethod
# class method takes cls as first parameter while instance method takes self as first parameter

# class Employee:
#     company = "Google"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     # instance method
#     def get_info(self):
#         return f"Name: {self.name}\n Age: {self.age}\n Company: {self.company}"
    
#     @classmethod
#     def change_company(cls,new_company):
#         cls.company = new_company

# e1 = Employee("Buddha", 22)
# e2 = Employee("Pawan", 23)
# print(e1.get_info())
# print(e2.get_info())
# Employee.change_company("Meta")
# print(e1.get_info())
# print(e2.get_info())


# another example

class Student:
    count = 0

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        Student.count += 1
    
    def get_info(self):
        return f"Name: {self.name}\n Marks: {self.marks}"
    
    @classmethod
    def get_count(cls):
        return f"Total students: {cls.count}"

s1 = Student("Buddha", 99)
s2 = Student("Pawan", 88)
s3 = Student("Rahul", 95)
print(s1.get_info())
print(s2.get_info())
print(s3.get_info())

print(Student.get_count())
