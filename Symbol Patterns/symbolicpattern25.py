print("Enter the no of rows: ")
a = int(input())
counter = 1
for i in range(0, a):
    for j in range(a, 0, -1):
        if j in range(a, counter, -1):
            print("*", end=" ")
        else:
            print(chr(j+64), end=" ")
    counter = counter + 1
    print()
