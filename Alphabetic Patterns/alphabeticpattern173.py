height = 5
for i in range(0, height):
    print("H", end="")
    for j in range(0, height):
        if ((j == height - 1) or (i == height // 2)):
            print("H", end="")
        else:
            print(end=" ")
    print()
