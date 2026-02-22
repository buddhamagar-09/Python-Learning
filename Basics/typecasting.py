# we generally use str(),int(),float(),bool() for typecasting

name = "Buddha Saru Magar"
age = 21
height = 5.4
is_student = True

height_int = int(height) # Typecasting float to int
age_str = str(age) # Typecasting int to str
is_student_str = str(is_student) # Typecasting boolean to str
print(f"My name is {name}, I am {age_str} years old, my height is {height_int} and it is {is_student_str} that I am a student.")
print(type(height_int)) # Output: <class 'int'>
print(type(age_str)) # Output: <class 'str'>
print(type(is_student_str)) # Output: <class 'str'>