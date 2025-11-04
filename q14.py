#Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number"))
result = num1 + num2
print("Result:", result)
if result == ("string, int, boleen"):
    print("Invalid character entered. Please enter a number")
