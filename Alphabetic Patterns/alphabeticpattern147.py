height = 5
for i in range(0, height):
    print("*", end="")
    for j in range(0, height):
        if ((j == height - 1) or (i == height // 2)):
            print("*", end="")
        else:
            print(end=" ")
    print()
