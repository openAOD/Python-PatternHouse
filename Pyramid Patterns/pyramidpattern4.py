print("Enter the number of rows: ")
n = int(input())
spaces = n
counter = 1
for i in range(0, n):
    for k in range(0, spaces):
        print(" ", end="")
    for j in range(0, counter):
        print(chr(i+65), end=" ")
    counter = counter + 1
    print()
    spaces = spaces - 1
