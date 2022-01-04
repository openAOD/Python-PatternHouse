print("Enter the number of rows: ")
n = int(input())
counter = 1
for i in range(1, n+1):
    for j in range(0, counter):
        if j % 2 != 0:
            print("*", end=" ")
        else:
            print(i, end=" ")
    counter += 1
    print()
