# creating a simple banking system

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit_money():
    amount = float(input("Enter the amount you want to deposit: "))
    if amount < 0:
        print("Invalid amount !!")
        return 0
    else:
        print(f"You have successfully deposited ${amount:.2f}")
        return amount

def withdraw_money(balance):
    amount = float(input("Enter the amount you want to withdraw: "))
    if amount < 0 :
        print("Withdraw amount is not valid: ")
        return 0
    elif amount > balance:
        print("Insufficient balance !!")
        return 0
    else:
        print(f"You have successfully withdrawn ${amount:.2f}")
        return amount

def main():
    balance = 0
    is_running = True
    run_again = True
    
    while run_again:
        while is_running:
            print("************Banking System*************")
            print("1 to deposit money: ")
            print("2 to show balance: ")
            print("3 to withdraw money: ")
            print("4 to Quit the Program: ")
            print("****************************************")

            choice = int(input("Enter the choice: "))
            match choice:
                case 1:
                    balance += deposit_money()    
                case 2:
                    show_balance(balance)
                case 3:
                    balance -= withdraw_money(balance)
                case 4:
                    is_running = False
                    print("Thank you for using our banking system !!")
                    print("*****************************************")
                case _:
                    print("Invalid Choice !!")
        again = input("Do you want to use this system again ? (Y/N): ")
        if again.lower() != 'y':
            run_again = False
            print("Byee See you again !!")
        else:
            is_running = True
            print("\n")
    
if __name__ == '__main__':
    main()



    