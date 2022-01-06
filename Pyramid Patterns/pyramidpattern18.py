print("Enter the number of rows: ")
n = int(input())
spaces = n + (n - 1)
counter = 1
for i in range(n, 0, -1):
    n = i
    for k in range(0, spaces):
        print(" ", end="")
    for j in range(0, counter):
        print(n, end=" ")
        n = n + 1
    counter = counter + 2
    print()
    spaces = spaces - 2
