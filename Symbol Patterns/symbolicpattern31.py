print("Enter the number of rows: ")
n = int(input())
counter = 1
for i in range(0, n):
    for j in range(0, n):
        if counter == 1:
            if j == 0:
                print("*", end=" ")
            else:
                print("#", end=" ")
        elif counter == 2:
            if j in range(0, 3):
                print("#", end=" ")
            else:
                print("*", end=" ")
        elif counter == 3:
            if j in range(0, 3):
                print("*", end=" ")
            else:
                print("#", end=" ")
    counter = counter + 1
    if counter > 3:
        counter = 1
    print()
