list1 = ["a", "b", "c", "d", 4, 5, "e", "f"]

for element in list1:
    print(element)

list2 = [
    ['A', 1],
    ['B', 2],
    ['C', 3],
    ['D', 4]
]

for item, lolly in list2:
    print(item)

dict1 = dict(list2)

for item, lolly in dict1.items():
    print(item)
    print(lolly)

for item in dict1:
    print(item)
print(dict1)

lists = [int, float, 'A', 5, 3, 22, 15, 64]

for item in lists:
    if str(item).isnumeric() and item > 6:
        print(item)

i = 0

while i < 45:
    print(i)
    i = i + 1
