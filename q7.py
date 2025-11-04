#Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
marks = float(input("Enter the students marks (0-100): "))
if marks >= 80:
       print("grade = A ") 
elif marks >= 60:
        print("grade = B ") 
elif marks >= 40:
        print("grade = C ") 
elif marks >= 30:
         print("grade = D ") 
else:
    print("grade = E")
    

        