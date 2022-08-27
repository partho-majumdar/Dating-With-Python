def my_func():
    var1 = 69
    var2 = int(input("Enter any number to compare: "))

    if var2 > var1:
        print(var2, "is greater than", var1)

    elif var2 == var1:
        print(var2, "is equal to", var1)

    else:
        print(var2, "is less than", var1)

    in_loop()


def in_loop():
    call_again = input(''' Do you want to compare again? Please type "y" for yes or "n" for no? ''')

    if call_again == "y":
        my_func()

    elif call_again == "n":
        print("See you later")

    else:
        in_loop()


my_func()
