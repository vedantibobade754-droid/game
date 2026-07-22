# Ask the user for the number of rows
rows = int(input("Enter the number of rows: "))

# Outer loop for rows
for i in range(rows):

    # Print spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Print stars
    for k in range(2 * i + 1):
        print("&", end="")

    # Move to the next line
    print()