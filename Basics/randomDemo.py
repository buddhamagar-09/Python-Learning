import random as rd


low = 1
high = 100

# r_number = rd.randint(low,high)
# r_number = rd.random()
options = ("rock","paper","scissors")
choice = rd.choice(options)

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

print(choice)
rd.shuffle(cards)
print(cards)