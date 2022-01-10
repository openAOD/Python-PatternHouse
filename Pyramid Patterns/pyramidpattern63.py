n = int(input("Enter the number of rows: "))
spaces = n
counter = 1
for i in range(1, n+1):
    for k in range(0, spaces):
        print(" ", end="")
    for j in range(1, counter+1):
        if i % 2 == 0:
            print("*", end=" ")
        else:
            print(i, end=" ")
    counter = counter + 1
    spaces = spaces - 1
    print()
