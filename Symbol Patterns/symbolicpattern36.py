print("Enter the no of rows: ")
a = int(input())
counter = 1
for i in range(0, a):
    n = counter + i
    if i % 2 == 1:
        counter = n
    for j in range(0, i + 1):
        if i % 2 == 0:
            print(str(counter) + "#", end=" ")
            counter += 1
        else:
            print(str(counter) + "#", end=" ")
            counter = counter - 1
    counter = n + 1
    print()
