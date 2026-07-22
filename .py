principal = 0
rate = 0
time = 0

# Ask the user to enter the principal amount
while principal <=0:
      principal = float(input("Enter the principal amount: "))
if principal <= 0:
      print("Principal can't be less than or equal to zero")

# Ask the user to enter the interest rate
while rate <= 0:
      rate = float(input("Enter the interest rate (%): "))
if rate <= 0:
      print("Rate can't be less than qual to zero")      

# Ask the user to enter the time in years
while time <= 0:
      time = int(input("Enter the time (years): "))
if time <= 0:
      print("Enter time in years")
# Compound interest formula
total = principal * pow((1 + rate / 100), time)

# Display the final amount with 2 decimal places
print(f"Final Amount = ${total:.2f}")