print("Enter the no of rows: ")
n = int(input())
for i in range(0, n):
    for j in range(0, i+1):
        if j % 2 == 0:
            print(j+1, end=" ")
        else:
            print("*", end=" ")
    print()
