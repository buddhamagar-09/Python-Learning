# take length and breadth as a input from the user and findout the area of the rectan

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
print(f"Th area of the rectangle is {area}cm²")

# que2
# shopping cart items

item = input("What items would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}s.")
print(f"you total price is {total} ")