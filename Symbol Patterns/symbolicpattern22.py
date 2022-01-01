print("Enter the no of rows: ")
a = int(input())
counter = 0
for i in range(a, 0, -1):
    for j in range(a, 0, -1):
        if j in range(a, counter, -1):
            print(chr(i+64), end=" ")
        else:
            print("*", end=" ")
    counter = counter + 1
    print()
