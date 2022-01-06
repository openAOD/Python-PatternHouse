print("Enter the number of rows: ")
n = int(input())
spaces = 1
counter = n
for i in range(0, n):
    for k in range(0, spaces):
        print(" ", end="")
    for j in range(0, counter):
        print(chr(j+65), end=" ")
    counter = counter - 1
    print()
    spaces = spaces + 1
