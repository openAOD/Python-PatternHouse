alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())

for i in range(0, n):
    for j in range(0,i+1):
        if(i%2!=0):
            print(alpha[i],end=" ")
        else:
            print(i+1,end=" ")
    print()
