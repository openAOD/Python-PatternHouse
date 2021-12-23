height = 5
for i in range(0, height):
    for j in range(0, height):
            if (i == 0 or i == height - 1):
                print("I", end="")
            elif (j == height // 2):
                print("I", end="")
            else:
                print(end=" ")
    print()
