special = "!@#$%^&*()-_=+[]{}|;:',.<>?/"

while True:
    password = input("Enter Password: ")

    if (len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in special for char in password)):

        print("✅ Strong Password")
        break

    else:
        print("❌ Weak Password")
        print("Try Again...\n")
