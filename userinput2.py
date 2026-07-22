#shopping cart
item = input("what item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("how many many would you like to buy?: "))

total = price * quantity 
print(f"you have brought {quantity} x {item}/s")
print(F"you have brought {total}")