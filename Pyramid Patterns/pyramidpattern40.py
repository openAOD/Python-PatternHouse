n = int(input("Enter the number of rows: "))
spaces = 1
counter = n + 4
for i in range(n, 0, -1):
    for k in range(0, spaces):
        print(" ", end=" ")
    for j in range(1, counter+1):
        print(chr(i+64), end=" ")
    counter = counter - 2
    spaces = spaces + 1
    print()
