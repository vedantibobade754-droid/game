#function = A block of reusable code place () after the function name to involve it

def happy_brithday(name, age):
    print(f"Happy Birthday to {name}! ")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()
happy_brithday("vedu", 20)
happy_brithday("kruni", 21)
happy_brithday("shiro", 5)  

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: { due_date}")
display_invoice("Vedu", 12.06, "01/01/2026")    