# ------------------R-1------------------
def plus(a, b):
    return a + b


# print(plus(5, 7))

# --------------------R-2-----------------
plus2 = lambda a, b: a + b
ans = plus2(10, 23)
# print(ans)


list1 = [[1, 14], [9, 11], [8, 23]]
list1.sort(key=lambda x: x[1])
print(list1)
