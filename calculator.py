running = True

while running:

    num1 = float(input("Enter first number: "))
    operator = input("Enter (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print(f"Answer = {num1 + num2}")

    elif operator == "-":
        print(f"Answer = {num1 - num2}")

    elif operator == "*":
        print(f"Answer = {num1 * num2}")

    elif operator == "/":
        print(f"Answer = {num1 / num2}")

    else:
        print("Invalid Operator")

    choice = input("Do you want to calculate again? (y/n): ").lower()

    if choice == "n":
        running = False

print("Thanks for using Calculator!")