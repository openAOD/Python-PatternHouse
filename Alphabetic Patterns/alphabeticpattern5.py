print("Enter the no of rows: ")
n = int(input())
k = 1
for i in range(0, n):
    for j in range(1, n+1):
        k = k + 1
        print(chr(k+63), end=" ")
    print()
