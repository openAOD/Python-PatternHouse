height = 5
counter = height // 2
for i in range(0, height):
    print("*", end="")
    for j in range(0, height + 1):
        if j == height:
            print("*", end="")
        elif (i >= height // 2) and (j == counter or j == height - counter - 1):
            print("*", end="")
        else:
            print(end=" ")
    if i >= height // 2:
        counter = counter + 1
    print()
