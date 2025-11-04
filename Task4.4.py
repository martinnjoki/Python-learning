value = input("Enter a value: ")
if isinstance(value, str):
    print("string detected")
elif isinstance(value, int):
    print("Integer detected")
else:
    print("Unknown Type")

