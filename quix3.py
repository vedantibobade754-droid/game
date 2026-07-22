
questions = (" HOW MANY ELEMENTS ARE IN THE PERIODIC TABLE?: ",
           "NATIONAL ANIMAL OF INDIA?: ",
           "HOW MANY COLOUR'S ARE IN THE RAINBOW?: ",
           "HOW MANY LETTER'S ARE THERE IN ALPHABET?: ",
           "NATIONAL BIRD OF INDIA?: ")
options = (("A.116 ", "B.117 ", "C.118 ", "D.119 "),
           ("A.CROCODILE", "B.DOG ", "C.GIRAFFE ", "D.TIGER "),
           ("A.4 ", "B.5 ", "C.7 ", "D.8 "),
           ("A.26 ", "B.30 ", "C.12 ", "D.28 "),
           ("A.PARROT ", "B.PEACOCK ", "C.CROW ", "D.EAGEL "))
answers = ("C", "D", "C", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")        
    question_num += 1    

print("-------------------")
print("       RESULTS     ")    
print("-------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()    

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()    

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")