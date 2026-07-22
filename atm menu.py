running = True

while running:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is ₹5000")

    elif choice == 2:
        print("Deposit Successful")

    elif choice == 3:
        print("Withdraw Successful")

    else:
        print("Invalid Choice")

    again = input("Go back to menu? (y/n): ").lower()

    if again == "n":
        running = False

print("Thank you for using ATM!")