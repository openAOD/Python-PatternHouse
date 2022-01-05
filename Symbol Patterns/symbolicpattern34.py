print("Enter the no of rows: ")
a = int(input())
counter = 1
for i in range(0, a):
    for j in range(0, i + 1):
        print(str(counter) + "#", end=" ")
        counter += 1
    print()
