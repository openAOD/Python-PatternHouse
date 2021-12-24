height = 5
for i in range(0, height):
    print("L", end="")
    for j in range(0, height+1):
        if (i == height - 1):
            print("L", end="")
        else:
            print(end=" ")
    print()
