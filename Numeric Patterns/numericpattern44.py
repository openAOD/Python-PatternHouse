print("Enter the no of rows and starting number respectively: ")
n, i = map(int, input().split())
for x in range(0, n):
    for j in range(0, x+1):
        if x == 1:
            i = i - 1
        print(i, end=" ")
        i = i + 1
    print()