height = 5
counter = 0
for i in range(0, height):
    print("*", end="")
    for j in range(0, height+1):
        if (j == height):
            print("*", end="")
        elif (j == counter):
            print("*", end="")
        else:
            print(end=" ")
    counter = counter + 1
    print()
