# iterables = an object or collction that can return its element one at a time allowing it to be iterated over a loop

# name = "Buddha Saru Magar"

# for letter in name:
#     print(letter)

user_details = {
    "name" : "Buddha Saru Magar",
    "age" : 21,
    "district" : "Nawalpur",
    "city" : "Gaindakot-1",
    "Phone" : "9812345432"
}

for value in user_details.values():
    print(value)


# membership operators
# in, not in
# used in string set tuple dictionary list

# example
name = "Buddha Saru Magar"
letter = input("Enter the letter : ")

if letter in name:
    print(f"{letter} was found in {name}")
else:
    print(f"{letter} was not found in {name}")


# another example
user_address = {
                "name" : "Buddha Magar",
                "district" :"Nawalpur",
                "Phone" : "9876765453",
                "city" : "Gaindakot-1"
}

if "city" in user_address:
    print(f"{user_address['city']}")
else:
    print("city not found")