n = 18
number_of_guess = 1
print("Number of guess is limited it took 9 times")

while number_of_guess <= 9:
    guess_number = int(input("Guess any number : "))
    if guess_number > 18:
        print("Guess smaller number")

    elif guess_number < 18:
        print("Guess greater number")

    else:
        print("You won")
        print(number_of_guess, "guess he/she took to finish")
        break

    print(9 - number_of_guess, "guess left")
    number_of_guess = number_of_guess + 1

if number_of_guess > 9:
    print("Game Over!")

#
# init_num = 69
# number_of_guess = 1
#
# print("Number of guess is limited it took 9 guess")
#
# while number_of_guess <= 9:
#
#     take_input = int(input("Guess the number: "))
#
#     if take_input > 69:
#         print("Guess smaller number!")
#
#     elif take_input < 69:
#         print("Guess bigger number!")
#
#     else:
#         print("You won!")
#
#         break
#     print(9 - number_of_guess, "guess left")
#     number_of_guess += 1
#
# if number_of_guess > 9:
#     print("Game over")
