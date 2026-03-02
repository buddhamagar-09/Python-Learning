# list comprehension = a concise way to create list in python
# compact and easier to read tha traditional loops
# [expression for value in iterable if codition]

# traditional way

numbers = []
for i in range(1,10):
    numbers.append(i * 2)
print(numbers)

# list comprehension way
numbers = [x * 2 for x in range(1,10)]
print(numbers)

animals = ["horse","cat","dog","banana","lion"]
animals = [animal.upper() for animal in animals]
animals_char = [animal[0] for animal in animals]
print(animals)
print(animals_char)

# working with if condition

numbers = [-1,0,2,5,6,-2,-7,9,-8]
positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num  for num in numbers if num % 2 != 0]

print(positive_numbers)
print(negative_numbers)
print(even_numbers)
print(odd_numbers)