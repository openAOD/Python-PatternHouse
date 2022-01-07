height = 5
space = height // 3
width = height // 2 + height // 5 + space + space
for i in range(0, height):
    for j in range(0, width + 1):
        if j == width - abs(space) or j == abs(space):
            print("*", end="")
        elif (i == 0 or i == height - 1) and j > abs(space) and j < width - abs(space):
            print("*", end="")
        else:
            print(end=" ")

    if space != 0 and i < height // 2:
        space = space - 1
    elif i >= (height // 2 + height // 5):
        space = space - 1

    print()

d = height
for i in range(0, height // 2):
    for j in range(0, d + 1):
        if j == d:
            print("*", end="")
        else:
            print(end=" ")
    print()
    d = d + 1
