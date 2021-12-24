height = 5
counter = 0
for i in range(0, height):
    print("M", end="")
    for j in range(0, height+1):
        if (j == height):
            print("M", end="")
        elif (j == counter or j == height - counter - 1):
            print("M", end="")
        else:
            print(end=" ")
    if(counter == height // 2):
        counter = -99999
    else:
        counter = counter + 1

    print()
