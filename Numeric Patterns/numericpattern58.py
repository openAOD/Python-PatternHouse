print("Enter the no of rows and starting number respectively: ")
n, i = map(int, input().split())
a = i
b = n
for j in range(0, n):
    for k in range(b, 0, -1):
        print(i, end=" ")
        i = i - 1
    i = a
    b = b - 1
    print()
