#Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254
phone_number = input("Enter the phone number: ")
if phone_number. startswith("+254"):
    print("A valid phone_number")
else:
    print("Invalid phone_number")