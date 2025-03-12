# Python Banking Program

def show_balance(balance):
    print("----------------------")
    print(f"Your current balance is ${balance:.2f}")


def deposit():
    print("----------------------")
    amount = float(input("Enter your amount to be deposited: "))

    if amount < 0:
        print("Amount must be greater than zero. Please enter a valid amount.")
        return 0
    else:
        return amount


def withdraw(balance):
    print("----------------------")
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient Fund!")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero. Please enter a valid amount.")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("----------------------")
        print("Banking Program Choice")
        print("----------------------")
        print("1: Show Balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Exit")

        print("----------------------")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            break
        else:
            print("Enter a valid choice!")

    print("----------------------")
    print("Thank you for using banking program!")


if __name__ == "__main__":
    main()
