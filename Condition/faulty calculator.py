def my_calc():
    print("Enter first number :", end=" ")
    num1 = int(input())
    print('Enter second number :', end=" ")
    num2 = int(input())
    print('So what you want?' + " " + '+,-,/,%,*')
    num3 = input()

    if num1 == 45 and num2 == 3 and num3 == '*':
        print("Addition of two number is : 555")
    elif num1 == 56 and num2 == 9 and num3 == '+':
        print("Sum of two number is : 77")
    elif num1 == 56 and num2 == 6 and num3 == '/':
        print("Divide of two number is : 4")
    elif num3 == '*':
        num4 = num1 * num2
        print("Addition of two number is : ", num4)
    elif num3 == '+':
        plus = num2 + num1
        print("Sum of two number is : ", plus)
    elif num3 == '/':
        div = num2 / num1
        print("Divide of two number is : ", div)
    elif num3 == '-':
        div = num2 - num1
        print("Subtract of two number is : ", div)
    elif num3 == '%':
        mod = num2 % num1
        print("Modulus of two number is : ", mod)
    else:
        print("Error! Please check your input")

    continue_loop()


def continue_loop():
    user_input = input(''' Do you want to calculate again? Please type "y" for yes or "n" for no? ''')

    if user_input == "y":
        my_calc()

    elif user_input == "n":
        print("Bye! see you later ^_^")

    else:
        continue_loop()


my_calc()

