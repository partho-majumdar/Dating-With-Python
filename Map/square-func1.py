num = [1, 2, 3, 4, 5]


def func1(a):
    return a * a


square = list(map(func1, num))
print(square)

num2 = [4, 5, 6, 7]
new_square = list(map(lambda x: x * x, num2))
print(new_square)
