print("Enter the no of rows: ")
n = int(input())
for i in range(n):
    count = i
    for j in range(i,n):
        print(j+1, end=" ")
    for j in range(i-1,0,-1):
        print(j);
    print("\n")
