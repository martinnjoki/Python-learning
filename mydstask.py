my_ds = [23, "jane", (560), ["lesson", "maths", {"currency":"KES"}], 987, (76, "JOHN")]
print(my_ds[3][2]["currency"])
print(my_ds[2])
print(my_ds[3][1])
my_ds[3][2]["amount"] = 90
print(my_ds)
my_ds[5] = (76,"Jane")
print(my_ds)
#slicing and stepping
name = "mbungu,njoki"
print(name[2:5])
print(name[6:8])
#changing a tuple to a list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] ="kiwi"
x = tuple(y)
print(x)
#condition statement
x = 100
y = 50
if x > y:
    print(f{x})

    print()
    


