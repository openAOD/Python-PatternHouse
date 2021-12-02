print("Enter the no of rows: ")
n = int(input())
k = 1
for i in range(0, n):
    for j in range(1, n+1):
        k = i + j
        print(chr(k+64), end=" ")
    print()
