# ATM

name = "Gabi Guimaraes"
iban = "123 456 789"
number = "0511 111 11 11"
balance = 2000

print("Welcome to the Bank !!!")
choice = input("Enter 's' to insert the card, 'a' to eject the card: ")

if choice == "s":
    while True:
        print("\n1- Withdraw Money")
        print("2- Deposit Money")
        print("3- Card Information")
        print("4- Card Return")
        action = input("Select the transaction to be made on the card: ")
        
        if action.isdigit():
            action = int(action)
        else:
            print("Invalid input. Please enter a number.")
            continue

        if action == 1:
            withdraw = input("How much money do you want to withdraw: ")
            if withdraw.isdigit():
                withdraw = int(withdraw)
                if withdraw <= balance:
                    balance -= withdraw
                    print("Updated Balance: ", balance)
                else:
                    print("Insufficient balance")
            else:
                print("Invalid input. Please enter a valid amount.")

        elif action == 2:
            deposit = input("How much money do you want to deposit: ")
            if deposit.isdigit():
                deposit = int(deposit)
                balance += deposit
                print("Updated Balance: ", balance)
            else:
                print("Invalid input. Please enter a valid amount.")

        elif action == 3:
            print("Name:", name)
            print("IBAN:", iban)
            print("Phone Number:", number)
            print("Balance:", balance)

        elif action == 4:
            print("Card return completed")
            break

        else:
            print("Invalid selection. Please choose a valid option.")

else:
    print("Card not inserted")
