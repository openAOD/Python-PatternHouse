print("Enter the no of rows: ")
a = int(input())
counter = 1
n = 1
for i in range(0, a):
    for j in range(0, n):
        if j % 2 == 1:
            print("*", end=" ")
        else:
            print(counter, end=" ")
            counter += 1
    counter = 1
    n += 2
    print()
