print("Enter the number of rows: ")
n = int(input())
counter = n
for i in range(0, n):
    for j in range(1, counter+1):
        if i % 2 != 0:
            print("*", end=" ")
        else:
            print(j, end=" ")
    counter = counter - 1
    print()
