#name = input("Enter your name: ")

#while name == "":
  #  print(f"You did not enter your name")
 #   name = input("Enter your name: ")
#else: 
   # print(f"Hello {name}")    

#age = int(input("Enter your age: "))   

#while age<0:
 #   print(f"Age can't be negative")
 #   age = int(input("Enter your age: "))
#else:
#    print(f"Your age is {age} years old")    

#food = input(f"Enter a food you like (q to quit):  ")

#while not food == "q":
 #   print(f"You like {food}")
 #   food = input(f"Enter a food you like (q to quit):  ")

#print(f"bye")

num = int(input("Enter number between 1 to 10: "))

while num < 1 or num > 10:
    print(f"{num} Is in-valid")
    num = int(input("Enter number between 1 to 10: "))

print(f"Your no is {num}")
