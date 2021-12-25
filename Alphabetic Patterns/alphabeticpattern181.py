height = 5
for i in range(0, height):
    print("P", end="")
    for j in range(0, height):
        if ((i == 0 or i == height // 2) and j < height - 1):
            print("P", end="")
        elif (i < height // 2 and j == height - 1 and i != 0):
            print("P", end="")
        else:
            print(end=" ")
    print()
