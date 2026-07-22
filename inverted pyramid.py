# Ask the user for the number of rows
rows = int(input("Enter the number of rows: "))

# Outer loop controls the rows
for i in range(rows, 0, -1):

    # Print stars
    for j in range(i):
        print("*", end="")

    # Move to the next line
    print()