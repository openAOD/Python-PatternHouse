n = int(input("Enter the number of rows: "))
spaces = n + (n - 1)
counter = 1
f = 1
b = n
for i in range(1, n + 1):
    for k in range(0, spaces):
        print(" ", end="")
    for j in range(0, counter):
        if j == i-1 or j > i-1:
            print(b, end=" ")
            b = b - 1
        else:
            print(b, end=" ")
            b = b + 1
    counter = counter + 2
    spaces = spaces - 2
    b = n - f
    f = f + 1
    print()
