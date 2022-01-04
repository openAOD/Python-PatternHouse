print("Enter the number of rows: ")
n = int(input())
counter = n
for i in range(n, 0, -1):
    for j in range(1, counter+1):
        if j % 2 == 0:
            print("*", end=" ")
        else:
            print(i, end=" ")
    counter = counter - 1
    print()
