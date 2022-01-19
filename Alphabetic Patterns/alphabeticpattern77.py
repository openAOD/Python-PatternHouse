alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())

for i in range(0, n):
    for j in range(0,n-i):
        if(i%2==0):
            print(alpha[j],end=" ")
        else:
            print(j+1,end=" ")
    print()
