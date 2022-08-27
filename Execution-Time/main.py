import time

initial1 = time.time()

k = 0
while k < 5:
    print("Inside while loop")
    time.sleep(1)
    k += 1

while_loop_time = time.time() - initial1
print(f"While loop take {while_loop_time} second")

initial2 = time.time()
for i in range(1, 6):
    print("Inside for loop")
    time.sleep(1)

for_loop_time = time.time() - initial2
print(f"For look take {for_loop_time} second")

if while_loop_time > for_loop_time:
    print("For loop is faster than while loop")

elif while_loop_time < for_loop_time:
    print("While loop is faster than for loop")

else:
    print("Both loop take same time")
