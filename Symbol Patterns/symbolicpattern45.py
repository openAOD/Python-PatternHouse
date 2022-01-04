print("Enter the number of rows: ")
n = int(input())
counter = n
c = n
for i in range(0, n):
    for j in range(0, counter):
        if i % 2 != 0:
            print("*", end=" ")
        else:
            print(c, end=" ")
    counter = counter - 1
    c = c - 1
    print()
