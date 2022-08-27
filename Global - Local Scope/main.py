x = 89


def function1():
    x = 20  # local

    def function2():
        global x
        x = 88  # global

    print("before calling function2() -->", x)

    function2()
    print("after calling function2() -->", x)


function1()
print(x)
