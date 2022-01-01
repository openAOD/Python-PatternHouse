print("Enter the no of rows: ")
a = int(input())
counter = 1
for i in range(0, a):
    for j in range(0, a):
        if j in range(0, counter):
            print(chr(i+65), end=" ")
        else:
            print("*", end=" ")
    counter = counter + 1
    print()
