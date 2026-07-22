word = "APPLE"
while True:
 letter = input("Guess a letter in the secret word: ")
 if letter in word:
    print(f"There is a {letter}")
 else:
     print(f"{letter} was not found") 

 choice = input(f"Enter again(y/n): ").lower() 
 if choice == "y": 
      print("Thanks for  Entering!")
 elif choice == "n":
    print("Quite")
    break
 else:
    print("Please enter again: ")
   