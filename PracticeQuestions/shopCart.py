# Shopping cart using list

items = []
quantities = []
prices = []
total = 0

while True:
    item = input("Enter the Items you want to add to cart or (q  to quit). ")
    if item.lower() == "q":
        break
    else:
       quantity = int(input("Enter the quantity: "))
       price = int(input(f"Enter the price of the {item}:"))
       items.append(item)
       quantities.append(quantity)
       prices.append(price)

print("...........Your Shopping cart ............")
for i in range(len(items)):
    total += prices[i] * quantities[i]
    print(f"{items[i]} x {quantities[i]} = Rs {prices[i] * quantities[i]}")

print(f"Your total amount is Rs {total}")

