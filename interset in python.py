# Ask the user to enter the principal amount
principal = float(input("Enter the principal amount: "))

while principal <= 0:
    print("Principal can't be less than or equal to zero")
    principal = float(input("Enter the principal amount: "))

# Ask the user to enter the interest rate
rate = float(input("Enter the interest rate (%): "))

while rate <= 0:
    print("Rate can't be less than or equal to zero")
    rate = float(input("Enter the interest rate (%): "))

# Ask the user to enter the time in years
time = int(input("Enter the time (years): "))

while time <= 0:
    print("Time can't be less than or equal to zero")
    time = int(input("Enter the time (years): "))

# Compound interest formula
total = principal * pow((1 + rate / 100), time)

# Display the final amount
print(f"Final Amount = ${total:.2f}")