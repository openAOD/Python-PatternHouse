height = 5
for i in range(0, height):
    for j in range(0, height):
        if ((i == 0 or i == height // 2 or i == height - 1)):
            print("S", end="")
        elif (i < height // 2 and j == 0):
            print("S", end="")
        elif (i > height // 2 and j == height - 1):
            print("S", end="")
        else:
            print(end=" ")
    print()
