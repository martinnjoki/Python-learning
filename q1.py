#Write a program that prompts the user to enter the base and height of a triangle and returns its area.
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
area = 0.5* base* height
print(f"The area of the triangle is: {area} ")
#function
def triangle_area(base, height):
    return 0.5 * base * height
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
area = triangle_area(base, height)
print(f"The area of triangle is {area}")
