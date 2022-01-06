print("Enter the number of rows: ")
n = int(input())
spaces = n + (n - 1)
counter = 1
f = 0
b = 0
for i in range(0, n):
    f = b
    for k in range(0, spaces):
        print(" ", end="")
    for j in range(0, counter):
        print(abs(f), end=" ")
        f = f - 1
    counter = counter + 2
    print()
    b = b + 1
    spaces = spaces - 2
