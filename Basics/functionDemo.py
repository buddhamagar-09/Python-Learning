import time as t

# function is a block of reusable code place () after the function name to invoke it
# parameterized function with arguments
# def happy_birthday(name,age):
#     for i in range(5,0,-1):
#         t.sleep(1)
#         print(i)
#     print(f"Happy Birthday {name}")
#     print(f"You are {age} years old now")

# happy_birthday("Buddha",20)

# return type
# statement used to end the function and return a value back to the caller

# def capitalize_name(first,last):
#     first_name = first.capitalize()
#     last_name = last.capitalize()
#     return first_name + " "+ last_name

# full_name = capitalize_name("buddha","saru")
# print(full_name)

# another example
# def sum(a,b):
#     return a+b
# def multiply(a,b):
#     return a * b
# print(sum(2,5))
# print(multiply(2,5))

# default arguments are used to make the function more flexible and can reduce the no of arguments
# def calculate_total(price,discount = 0,tax = 0.13):
#     return price * (1 - discount) * (1 + tax)

# print(calculate_total(2000))

# another example
# def count(start,end):
#     for x in range(start,end+1):
#         t.sleep(1)
#         print(x)
#     print("Done!")

# count(0,5)


# Keyword Arguments is an argumnent precedded by an identifier which helps in readibility and order of arguments doesnt matter

def display_book(name,genre,author,price):
    print(f"{name} : {genre} : {author} : {price}")

display_book("Love Attack",genre="romance",price=1000,author="Buddha Saru Magar")
 

#  another example

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

my_phone = get_phone(country=1,area=321,first=977,last=921)
print(my_phone)