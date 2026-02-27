# creating a food menu using a dictionary

menus = {
        "burger" : 250,
        "pizza" : 500,
        "katti Roll" : 150,
        "momo" : 150,
        "chowmein" : 80,
        "beer" : 300,
        "thukpa" : 120,
        "chicken Tandori" : 450
}

cart =  []
total = 0

print("-------Menu-------")
for key , value  in menus.items():
    print(f"{key:10} : {value}")

print("--------------------")
while True:
    item = input("Select an item or type q for quit: ").lower()
    if item == "q":
        break
    elif menus.get(item) is not None:
        cart.append(item)

print("......You ordered.......")
for cartitems in cart:
    total += menus.get(cartitems)
    print(cartitems, end=" ")

print()
print(f"Your Total is Rs. {total}")


