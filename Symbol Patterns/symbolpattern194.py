height = 5
count= 0
for i in range(0, height):
    print("*", end="")
    for j in range(0, height+1):
        if (j == height):
            print("*", end="")
        elif (j == count):
            print("*", end="")
        else:
            print(end=" ")
    count = count + 1
    print()
