height = 5
for i in range(0, height):
    print("F", end="")
    for j in range(0, height):
        if ((i == 0) or (i == height // 2 and j <= height // 2)):
            print("F", end="")
        else:
            continue
    print()
