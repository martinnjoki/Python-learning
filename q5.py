#Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
largest = "num1"
if num2 < largest:
    largest = num2
if num3 < largest:
    largest = num3
    print(" The largest number is: Largest")
else:
    print("The smallest number")
