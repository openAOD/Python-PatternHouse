height = 5
width = 2*height - 1
counter = 0
for i in range(0, height):
    for j in range(0, width + 1):
        if j == counter or j == width - counter - 1:
            print("*", end="")
        else:
            print(end=" ")

    counter = counter + 1
    print()
