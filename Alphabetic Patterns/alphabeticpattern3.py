print("Enter the no of rows: ")
n = int(input())
for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        print(chr(i+64), end=" ")
    print()
