height = 5
width = 2*height - 1
half = (height // 2)
for i in range(0, height):
    print("R", end="")
    for j in range(0, width):
        if ((i == 0 or i == half) and j < (width - 2)):
            print("R", end="")
        elif (j == (width - 2) and not(i == 0 or i == half)):
            print("R", end="")
        else:
            print(end=" ")
    print()
