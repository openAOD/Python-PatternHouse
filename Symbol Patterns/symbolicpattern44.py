print("Enter the number of rows: ")
n = int(input())
counter = n
for i in range(0, n):
    for j in range(0, counter):
        if j % 2 != 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    counter = counter - 1
    print()
