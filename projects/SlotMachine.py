import random
import time as t

def spin_row():
    symbols = ["⭐","🔔", "🌳" ,"☀️"]
    result = []

    for symbol in range(3):
        result.append(random.choice(symbols))
    return result


def print_row(row):
    print("******************************")
    print("       "+"  |  ".join(row))
    print("******************************")

def payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "⭐":
            return bet * 3
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "🌳":
            return bet * 3
        elif row[0] == "☀️":
            return bet * 3
    return 0

def main():
    balance = 100
    print("******************************")
    print("python SlotMachine Game")
    print("Symbols: ⭐ 🔔 🌳 ☀️ ")
    print("******************************")
    print("Rules:\n " 
    "Get all 3 symbols same to triple your bet amount.\n " 
    "Get all symbols bell to get 10 X bonus of your bet.")
    while balance > 0:
        print(f"Your Current balance is: ${balance}")

        bet = (input("Enter your bet: "))

        if not bet.isdigit():
            print("Enter a proper bet..")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient Balance")
            continue 
        if bet <= 0 :
            print("Invalid Balance amount !!")   

        balance -= bet
        row = spin_row()
        print(".........Spinning............")
        t.sleep(1)
        print_row(row)

        money_win = payout(row,bet)
        if money_win > 0 :
            print(f"You have just won ${money_win}")
        else:
            print("You have lost your bet")
        balance += money_win
        print(f"Your remaining Balance : ${balance}")
        play_again = input("Do you Want to Play again ? (Y/N): ").upper()
        if play_again != "Y" :
            break

    print("******************************")
    print(f"Your Current Balance is ${balance}")
    print("Thank You For playing this game:😊")


if __name__ == "__main__":
    main()
