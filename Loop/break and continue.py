# break --> stop the loop
# continue --> skip

i = 0

while True:
    if i < 5:
        i += 1
        continue
    print(i, end=" ")
    if i == 24:
        break
    i += 1

while True:
    take_input_from_user = int(input("Enter any number \n"))
    if take_input_from_user > 100:
        print("Congrats!")
        break
    else:
        print("Try again")
        continue
