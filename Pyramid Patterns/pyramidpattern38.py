n, h = map(int, input("Enter the number of rows and starting number respectively: ").split(" "))
spaces = 1
counter = n + 4
a = 64
for i in range(n, 0, -1):
    b = i
    for k in range(0, spaces):
        print(" ", end=" ")
    for j in range(0, counter):
        print(h, end=" ")
    counter = counter - 2
    spaces = spaces + 1
    h = h - 2
    print()
