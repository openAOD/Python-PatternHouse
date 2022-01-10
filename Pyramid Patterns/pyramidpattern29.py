n = int(input("Enter the number of rows: "))
spaces = n + (n - 1)
counter = 1
for i in range(1, n + 1):
    b = i
    for k in range(0, spaces):
        print(" ", end="")
    for j in range(0, counter):
        print(chr(i+64), end=" ")
    counter = counter + 2
    spaces = spaces - 2
    print()
