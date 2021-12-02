print("Enter the no of rows: ")
n = int(input())
for i in range(1, n+1):
    k = 2
    for j in range(1, i+1):
        print(k, end=" ")
        k = k + 2
    print()
