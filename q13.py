#Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
target_email = "admin@gmail.com"
target_password = "Admin@123"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    email = input("Enter email: ")
    password = input("Enter password: ")
if email == target_email and password == target_password:
    print("login is successful")
else:
    attempts += 1
    remaining = max_attempts - attempts
    if remaining > 0:
        print("Invalid username or password.", remaining, "attempts left.")
    else:
        print("You have been blocked. Maximum attempts reached. ")



