print("Enter the no of rows and starting number respectively: ")
n, i = map(int, input().split())
a = 3
b = i
for x in range(0, n):
    for j in range(0, x+1):
        if x > 0:
            i = b + a
            a = a + 2
            b = i
        print(i, end=" ")
    print()
