grades = {
    "veda": "A",
    "xyz": "B",
    "lmn": "C",
    "pqr": "D"
}

while True:

    student = input("Enter the name of a student (or q to quit): ").lower()

    if student == "q":
        print("Goodbye!")
        break

    if student in grades:
        print(f"{student}'s grade is {grades[student]}")
    else:
        print(f"{student} was not found")
        