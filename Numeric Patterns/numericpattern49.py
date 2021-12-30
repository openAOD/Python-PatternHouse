print("Enter the number of rows:")
n = int(input())
a = 0
for i in range(0, n):
    for j in range(0, i+1):
        if i % 2 == 0:
            a = 0
        else:
            a = 1
        print(a, end=" ")
    print()
