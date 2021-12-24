height = 5
counter = 0
for i in range(0, height):
    print("*", end="")
    for j in range(0, height+1):
        if (j == height):
            print("*", end="")
        elif (j == counter or j == height - counter - 1):
            print("*", end="")
        else:
            print(end=" ")
    if(counter == height // 2):
        counter = -99999
    else:
        counter = counter + 1

    print()
