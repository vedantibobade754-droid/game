print("Welcome to the Python Quiz!")

score = 0

answer = input("1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. Which language are you learning? ")

if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. How many days are there in a week? ")

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print(f"\nYour final score is {score}/3")