n = int(input("Number of rows: "))
k = -1
for i in range(n-1,-1,-1):
    for j in range(k,-1,-1):
        print(end=" ")
    k = k + 2
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")
k = 2 * n - 2
for i in range(1, n):
    for j in range(2, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
            print("* ", end="")
    print("\r")