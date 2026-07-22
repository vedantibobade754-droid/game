#temp = float(input("Enter the Temperature: "))
#unit = input("Is this temperature in celcius or fahrenhite (C/F): ")

#if unit == "C":
    #temp =round((9*temp)/5+32,1)
   # print(f"The temp is fahrenheit is: {temp} F")
#elif unit == "F":
    #temp = round((temp-32)*5/9,1)
    #print(f"The temp in celsius is: {temp} C")
#else:
   # print(f"{unit} is an invalid unit of measurement ")

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")