# l = 12  # global
#
#
# def func1():
#     l = 20  # local
#     m = 18  # local
#
#     print(l, m)
#
#
# func1()
# print(l)


l = 12  # global


def func1():
    global l
    l = l + 14  # global
    m = 18  # local

    print(l, m)


func1()
print(l)
