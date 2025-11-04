start_date = (input("Enter the start_date_obj: "))
end_date = (input("Enter the end_date_obj: "))
if start_date < end_date:
    print("valid period")
elif start_date > end_date:
    print("invalid period")
else:
    print("one day period")