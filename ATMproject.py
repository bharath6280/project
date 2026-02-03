# Account details
owner = "Bharath"
balance = 0

def show_menu():
    print("\n==============================")
    print("Welcome to ATM")
    print("Account Holder:", owner)
    print("==============================")
    print("1. Credit (Deposit)")
    print("2. Debit (Withdraw)")
    print("3. Check Balance")
    print("4. Exit")


def credit():
    global balance
    amount = float(input("Enter amount to credit: "))

    if amount <= 0:
        print("Amount must be greater than zero.")
    else:
        balance += amount
        print("Amount credited successfully.")
        print("Updated Balance: ", balance)


def debit():
    global balance
    amount = float(input("Enter amount to debit: "))

    if amount <= 0:
        print("Amount must be greater than zero.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Amount debited successfully.")
        print("Updated Balance: ", balance)


def check_balance():
    print("Account Holder:", owner)
    print("Current Balance: ", balance)


def atm():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            credit()
        elif choice == '2':
            debit()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            print("Thank you,", owner)
            print("Please visit again.")
            break
        else:
            print("Invalid choice. Please enter 1 to 4.")


atm()
          


