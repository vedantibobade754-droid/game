#name = input("Enter your full name: ")
#phone_no = input("Enter your phone: ")
#result = len(name)
#result = name.find("e")
# = name.rfind("d")                finding the position of any letter in the name
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()
#result = phone_no.count("-")
#result = phone_no.replace("-", " ")
#print(result)

#valid input exercise

username = input("Enter your name: ")

if len(username) > 5:
    print(f"Your username can't be more than 5 characters ")
elif not username.find(" ") == -1:
    print(f"Your username can't contain space")
elif not username.isalpha():
    print(f"Your username can't contain numbers")
else:
    print(F"Welcome {username}")    
