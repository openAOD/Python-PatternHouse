print("Enter the no of rows: ")
a = int(input())
b = a
for i in range(0, a):
    for j in range(0, a):
        if j in range(0, b):
            print(chr(j+65), end=" ")
        else:
            print("*", end=" ")
    b = b - 1
    print()
