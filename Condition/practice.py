def function1():
    age = int(input("Enter your age : "))

    if 7 < age < 18:
        print("You can't drive")

    elif 18 < age < 100:
        print("You can drive")

    elif age == 18:
        print("Come for physical test")

    else:
        print("Not a valid age")

    for_loop()


def for_loop():
    call_again = input("Want to calculate again type 'y' for yes and 'n' for no? ")

    if call_again == 'y':
        function1()

    elif call_again == 'n':
        print("Okay bye!")

    else:
        for_loop()


function1()
