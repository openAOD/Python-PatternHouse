height = 5
counter = 0
for i in range(0, height + 1):
    for j in range(0, height + 1):
        if j == counter or j == height - counter:
            print("*", end="")
        else:
            print(end=" ")
    counter = counter + 1
    print()
