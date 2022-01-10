n = 6
counter = 3
iterations = 0
for i in range(0, n):
    for j in range(0, counter):
        if counter == 2 and j == 0:
            print(end="  ")
        elif counter == 1:
            print(end="    ")
        print("*", end=" ")
    iterations = iterations + 1
    if iterations % 2 == 0:
        counter = counter - 1
    print()
