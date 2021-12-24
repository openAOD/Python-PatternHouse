height = 5
for i in range(0, height):
    print("*", end="")
    for j in range(0, height+1):
        if (i == height - 1):
            print("*", end="")
        else:
            print(end=" ")
    print()
