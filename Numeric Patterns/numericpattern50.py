print("Enter the number of rows:")
n = int(input())
a = 1
for i in range(0, n):
    for j in range(0, i+1):
        if i % 2 == 0:
            a = 1
        else:
            a = 0
        print(a, end=" ")
    print()