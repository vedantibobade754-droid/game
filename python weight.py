#python weight converter
weight = 45
#1 kg = 2.205 pounds
#50 × 2.205 = 110.25 pounds

weight = 50
weight = weight * 2.205

#print(weight)
#o/p=110.25

#110.25 ÷ 2.205 = 50 kg
weight = 110.25

weight = weight / 2.205

#print(weight)
#o/p=50.0

# Ask the user to enter their weight
weight = float(input("Enter your weight: "))

# Ask the user whether the weight is in Kilograms or Pounds
unit = input("Kilograms or Pounds? (K or L): ")

# If the user entered K, convert Kilograms to Pounds
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")

# If the user entered L, convert Pounds to Kilograms
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")

# If the user enters anything other than K or L
else:
    print(f"{unit} was not valid")


    