n = int(input("Number of rows: "))
k = 2 * n - 2
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print("*", end=" ")
    print("\r")
k = n - 2
for i in range(n-2, -1 , -1):
    for j in range(k , -2 , -1):
        print(end=" ")
    k = k + 1    
    for j in range(0, i+1):
        print("* " , end="")
    print("\r") 