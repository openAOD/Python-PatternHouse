print("Enter the no of rows: ")
a = int(input())
counter = 0
for i in range(0, a):
    b = 0
    for j in range(0, a):
        if j in range(counter, a):
            print(chr(b+69), end=" ")
        else:
            print("*", end=" ")
        b = b - 1
    counter = counter + 1
    print()
