print("Enter the no of rows: ")
n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        print(chr(i+64), end=" ")
    print()
