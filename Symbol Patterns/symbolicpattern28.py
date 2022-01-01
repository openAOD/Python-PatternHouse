print("Enter the no of rows: ")
a = int(input())
b = a
for i in range(0, a):
    for j in range(1, a+1):
        if j == b:
            print("*", end=" ")
        else:
            print(j, end=" ")
    b = b - 1
    print()
