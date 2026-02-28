import random as rd

low = 1
high = 100
guess = 0
r_number = rd.randint(low,high)

print("-----------------Number Guessing Game-------------------")
print(f"You have 5 attempts to guess the number between {low} and {high}")
for i in range(5):
    guess += 1
    number = int(input(f"Enter the number between {low} and {high}: "))
    if number < low or number > high:
        print("Invalid input! Please enter a number between 1 and 20.")
    elif number > r_number:
        print("Number too high: ")
    elif number < r_number:
        print("Number too low: ")
    else:
        print("You win!")
        print(f"The number was {number}")
        print(f"You guessed the number in {guess} attempts")
        break
else:
    print("You lose!")
    print(f"The number was {r_number}")

