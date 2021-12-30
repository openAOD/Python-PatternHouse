print("Enter the number of rows:")
n = int(input())
a = 0
for i in range(0, n):
    for j in range(0, i+1):
        if j == 1 or j == 2:
            a = 1
        elif j > 2:
            a = a + 1
        print(a, end=" ")
    counter = 1
    print()
