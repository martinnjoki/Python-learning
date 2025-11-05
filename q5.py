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
    #function
    def find_largest(num1, num2, num3):
        return max(num1, num2, num3)
    num1 = float(input("Enter the number: "))
    num2 = float(input("Enter the number: "))
    num3 = float(input("Enter the number: "))
    largest = find_largest(num1, num2, num3)
    print(f"The largest number is {largest}")
