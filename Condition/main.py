age = int(input("Enter your age: "))
if 18 < age < 101:
    print("you can drive")
elif 7 < age < 18:
    print("you can't drive")
elif age == 18:
    print("come for physical test")
else:
    print("not a valid age")

