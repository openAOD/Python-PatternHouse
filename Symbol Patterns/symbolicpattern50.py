print("Enter the number of rows: ")
n = int(input())
spaces = n
counter = 1
c = 0
for i in range(0, n):
    c = i + 1
    for k in range(0, spaces):
        print(" ", end=" ")
    for j in range(0, counter):
        if c % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
        c = c + 1
    counter = counter + 1
    print()
    spaces = spaces - 1
