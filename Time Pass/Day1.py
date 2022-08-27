# input1 = int(input("Enter first number: "))
# input2 = int(input("Enter second number: "))
#
# ans = input1 * input2
# print(ans)
#
#
# string1 = "Harry vhai is awesome"
# print(string1[0:3])  # index start from 0
# print(string1[0:6:2])
# print(string1[::-1])
# print(len(string1))
#
# string2 = "Hi my name is partho"
# print(string2.isnumeric())
# print(string2.isalnum())
# print(string2.isalpha())
#
# print(string2.lower().startswith("hi"))
#
# print(string2.replace("partho", "kunal"))
#
# bro = [
#     "hridoy", 22, "ananda", 23, "sushanta", 21, "nodip", 14
# ]
# bro[0] = "ajoy"
# bro.append("prodip")
# print(bro)
# print(bro[::-1])
# print(type(bro))
# print(bro[0])
# print(bro[1])
#
# list1 = [1, 2, 3, 4, 5, 6]
# (list1.insert(3, 33))
# list1.append(11)
# list1.pop()
# print(list1)
#
# # list --> mutable --> can change
# # tuple --> immutable --> can not change
#
# tuple1 = (1, 2, 3, 4, 5, 6)
# print(tuple1[::-1])
# tuple1[1] = 22
# print(tuple1)
#
# a = 7
# b = 2
# a, b = b, a
# print(a, b)
#
# tuple2 = ("a", "b", "c", 5)
# print(tuple2)
# print(list(tuple2))
#
# info = ("John", 28, "Alto")
# (name, age, university) = info
# print("My name is", name + "I am", age)
# print(f"My name is {name}. I am {age}. Currently study at {university} university") # this is known asf string
#
# # Dictionary is nothing but key-value pair
#
# dict1 = {"Partho": "cse",
#          "Hridoy": "BBA",
#          "Kakon": "MBBS",
#          "Ananda": {
#              "Home": "Bhola",
#              "Age": 22,
#              "Married": False
#          }}
# dict1["Khaled"] = "EEE"
# dict1[420] = 120
# print(dict1)
# del dict1[420]
# print(dict1)
#
# dict2 = {"Partho": "CSE",
#          "Hridoy": "BBA",
#          "Kakon": "MBBS",
#          }
#
# take_input = input("Enter student name: ")
# ans = take_input.capitalize()
# print(dict2[ans])
# copy_dict2 = dict2.copy()
# print(copy_dict2.items())
# print(copy_dict2.keys())
# print(copy_dict2.values())
# print(copy_dict2)
#
# # Set return unique value
#
# set1 = {1, 2, 3, 4, "a"}
# set1.add(7)
# set1.add("b")
# print(set1)
#
# var1 = 10
# var2 = 20
#
# if var1 > var2:
#     print("var1 is greater")
#
# elif var1 < var2:
#     print("var1 is smaller")
#
# else:
#     print("var1 and var2 is equal")
#
#
# loop1 = ["A", "B", "C", "D"]
# for element in loop1:
#     print(element)
#
# loop2 = [
#     ["A", 1],
#     ["B", 2],
#     ["C", 3],
#     ["D", 4]
# ]
#
# for value, number in loop2:
#     print(value)
#     print(number)
#
# loop3 = [
#     ["A", 1],
#     ["B", 2],
#     ["C", 3],
#     ["D", 4]
# ]
#
# make_dict = dict(loop3)
# print(make_dict)
#
# for ele in make_dict.items():
#     print(ele)
#
# for element2 in make_dict.values():
#     print(element2)
#
# for element3 in make_dict.keys():
#     print(element3)
#
# i = 0
#
# while True:
#     if i < 12:
#         print(i)
#     i += 1
#
# while True:
#     get_input = int(input("Enter any number: "))
#     if get_input > 100:
#         print("Congratulation")
#         break
#     else:
#         print("Try again")
#         continue
#
#
# main_number = 29
# number_of_guess = 1
# print("You have 10 life to guess the number")
#
# while number_of_guess <= 10:
#     guess_number = int(input("Guess any number: "))
#     if guess_number > 29:
#         print("Enter smaller number")
#
#     elif guess_number < 29:
#         print("Guess bigger number")
#
#     else:
#         print("You won")
#         print(number_of_guess, "guess you took to finish")
#
#     print(10 - number_of_guess, "life left")
#     number_of_guess += 1
#
# if number_of_guess > 10:
#     print("Game over")


# def function1(a, b):
#     """This function calculate average"""
#     avg = (a + b) / 2
#     return avg
#
#
# ans = function1(16, 18)
# print(ans)
# print(function1.__doc__)

# f = open("partho.txt", "rt")
# content = f.read(5)
# f.write("Partho is a good boy")
# print(content)
# print(f.readline())
# print(f.readlines())
# f.close()













