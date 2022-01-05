print("Enter the number of rows: ")
n = int(input())
spaces = n
counter = 1
c = 0
for i in range(0, n):
    c = i + 1
    for k in range(0, spaces):
        print(" ", end=" ")
    for j in range(1, counter+1):
        if i % 2 != 0:
            print("*", end=" ")
        else:
            print(c, end=" ")
        c = c - 1
    counter = counter + 1
    print()
    spaces = spaces - 1
