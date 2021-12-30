print("Enter the no of rows and starting number respectively: ")
n, i = map(int, input().split())
counter = 1
for x in range(0, n):
    for j in range(0, counter):
        print(i, end=" ")
        i = i - 1
    counter = counter + 1
    print()
