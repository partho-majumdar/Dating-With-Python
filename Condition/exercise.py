take_input = int(input("How many row you want to print? "))
take_bool = int(input("Type 1 for true and 0 for false! "))

if take_bool == 1:
    for element in range(1, take_input + 1):
        print(element * "* ")

if take_bool == 0:
    for element in range(take_input, 0, -1):
        print(element * "# ")
