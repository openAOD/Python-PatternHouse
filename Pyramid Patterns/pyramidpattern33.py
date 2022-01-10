n = int(input("Enter the number of rows: "))
spaces = n + (n - 1)
counter = 1
a = 64
for i in range(1, n + 1):
    b = i
    for k in range(0, spaces):
        print(" ", end="")
    for j in range(0, counter):
        if j == i-1 or j > i-1:
            print(chr(b+a), end=" ")
            b = b + 1
        else:
            print(chr(b+a), end=" ")
            b = b - 1
    counter = counter + 2
    spaces = spaces - 2
    print()
