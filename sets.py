numbers = {100,34,50,78, 'twenty'}
print(numbers)
print(type(numbers))
#add
numbers.add("five")
print(numbers)
#update
numbers.update([200,300,500])
print(numbers)
#remove
numbers.remove('twenty')
print(numbers)
#discard
numbers.discard(200)
print(numbers)
#dictionaries
person = {
    "name":"Mbungu",
    "Age":35,
    "Address":"68-10309 kiamutugu",
    "Married":False,
    "Friends":["God","Jesus christ"]
}
print(person)
print(type(person))
print(person["name"])
print(person["Age"])
print(person.get("Address"))
print(person.get("Married"))
#add
person["id"] = 2345
person["Age"] = 45
print(person)
#update
person.update({"name":"Lucy", "Age":39, "married":True})
print(person)
#.pop("key")
person.pop("Age")
print(person)
#.pop item
person.popitem()
print(person)
