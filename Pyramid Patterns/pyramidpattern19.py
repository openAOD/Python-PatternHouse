print("Enter the number of rows: ")
n = int(input())
f = n
spaces = n + (n - 1)
counter = 1
for i in range(n, 0, -1):
    a = f
    for k in range(0, spaces):
        print(" ", end="")
    for j in range(0, counter):
        print(a, end=" ")
        a = a - 1
    counter = counter + 2
    print()
    f = f + 1
    spaces = spaces - 2
