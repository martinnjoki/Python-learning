#Write a program that prints the largest of 4 inputs taken as input from a user.
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
largest = num1
if num2 < largest:
    largest = num2
if num3 < largest:
    largest = num3
if num4 < largest:
    largest = num4
    print("largest number:", largest)