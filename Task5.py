student_score = int(input("Enter student score"))
attendance = int(input("Enter the student's attendance"))
if student_score > 90 and attendance > 80:
    print("Excellent student")
elif student_score > 90 and attendance < 80:
    print("Good score but attendance needs improvement")
else:
    print("Invalid Score- score below 90")
    