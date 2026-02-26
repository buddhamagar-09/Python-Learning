# collection = a data structure that can hold more than one value at a time
# list = [] a collection which is ordered and changeable. Allows duplicate members.
#tuple =() a collection which is ordered and unchangeable. Allows duplicate members.
#set = {} a collection which is unordered and unindexed. No duplicate members. allow to add and remove 
#dictionary =  a collection which is ordered and changeable. No duplicate members.

# list example
# animals = ["cat","baboon","elephant","dog"]

# animals.reverse()
# animals.append("fox")
# animals.remove("fox")
# animals.insert(0,"snake")
# animals.sort()
# print(len(animals)) //4
# print("crocs" in animals) //false
# for animal in animals:
#     print(animal)
# print(animals)

# Set example
# fruits = {"apple","banana","grapes","orange"}
# fruits.pop()
# fruits.remove("apple")
# fruits.add("watermelon")
# fruits.clear()
# print(len(fruits))
# print(fruits)
# for fruit in fruits:
#     print(fruit)


# tuple example 
# fruits = ("apple","banana","grapes","coconut")
# print(fruits)
# print("apple" in fruits)
# print(fruits.index("apple"))
# print(fruits.count("apple"))

# for fruit in fruits:
#     print(fruit)



# 2d collection example

vegetables = ["potato","onion","beans"]
fruits = ["orange","mango","watermelon"]

# greoceries = [vegetables,fruits]
# print(greoceries[0])

# or
groceries = [["potato","onion","beans"],
              ["orange","mango","watermelon"]]

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()





