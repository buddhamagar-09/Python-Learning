import random as rd

options = ("rock","paper","scissors")
play_game = True

while play_game:
    userscore = 0
    computerscore = 0
    is_running = True

    print("----------------Rock Paper Scissors Game-----------------")
    while is_running:
        user_choice = input("Enter your Choice:  or type q to quit the game: ").lower()
        if user_choice == "q":
            is_running = False
            continue
        
        computer_choice = rd.choice(options)
        print(f"User Choice: {user_choice}")
        print(f"Computer Choice: {computer_choice}")
        
        if user_choice not in options:
            print("Invalid input! Please enter a valid choice: Rock, Paper, or Scissor.")
        elif user_choice == computer_choice:
            print("Its a Draw: ")
        elif user_choice =="rock" and computer_choice == "scissors"  or user_choice == "paper" and computer_choice == "rock"   or user_choice == "scissors" and computer_choice == "paper":
            userscore += 1
            print(f"User Win !")
        else:
            computerscore += 1
            print("Computer Won")

    if userscore == computerscore:
        print("Its a Draw!! Try again")
    elif userscore > computerscore:
        print("User Won this Competition!!")        
    else:
        print("Computer Won this Competition!! Try again")
    print(f"userscore: {userscore} || computerscore: {computerscore}")

    playAgain = input("\nWould you Like to Play Again (y/N): ").lower()
    if playAgain != "y":
        play_game = False
        print("Thanks for playing! Goodbye!")
    else:
        print("\n")
else:
    is_running = False
    print("Thank Your For Playing The game. See you Soon!")