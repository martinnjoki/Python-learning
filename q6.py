#Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
correct_password = "admin@123"
max_attempts = 4
attempts = 0
while attempts < max_attempts:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted")
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"incorrect password. {remaining_attempts} attempts remaining")
        else:
            print("Account blocked. Maximum attempts reached")