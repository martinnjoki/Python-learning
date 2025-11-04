
numbers = []
for i in range(1, 51):
    numbers.append(i)
print(numbers)

list2 = []
for number in numbers:
    if number % 5 == 0 or number % 7 == 0:
        list2.append(number)
print(list2)

list3 = []
for x in list2:
   if x % 2 == 0:
    list3.append(x)
print(list3)
#nested loop
for i in range(2):
   for j in range(3):
      print(i,j) 
      #Area of a triangle
      base = int(input("Enter the base: ")) 
      height = int(input("Enter the height: "))
      area = 0.5 * base * height
      print(f"The area of the triangle is: {area}") 

                     
                     
      
      
      
                    
                

    