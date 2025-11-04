#Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
speed = float(input("Enter car speed (km/h): "))
if speed <= 70:
    print("OK")  
else:
    demerit_points = int((speed-70) / 5)
    print(f"Demerit points: {demerit_points}")
if demerit_points > 12:
    print("licence suspended")
 


    