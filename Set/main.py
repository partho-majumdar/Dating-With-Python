var1 = [1, 2, 3, 4, 5]  # list --> mutable --> can change
var2 = {1, 2, 3, 4, 5}  # set --> return unique value
var3 = (1, 2, 3, 4, 5)  # tuple --> immutable --> cannot change
var4 = {  # dictionary --> keys values pair
    "Partho": "cse",
    "Skib": "me",
    "Ausru": "ipe",
    "Age": 20,
    "Hridoy": {
        "Home": "Ulania",
        "Work": "Business",
        "Age": 22
    }
}

# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))

var5 = {1, 2, 3, 4, 5}
var5.add(11)
var5.add(31)
print(var5)

new_union = var5.union({1, 2, 3})
new_intersection = var5.intersection({3, 31})
print(new_union)
print(new_intersection)











