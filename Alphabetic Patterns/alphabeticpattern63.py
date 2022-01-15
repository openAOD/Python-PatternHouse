
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())
for i in range(0, n):
    for k in range(0,n-i-1):
        print("*",end=" ")
    count = i
    for j in range(0, i+1):
        print(alpha[count], end=" ")
        count-=1
    print()
    
# Enter the no of rows: 
# 5
# * * * * A 
# * * * B A 
# * * C B A 
# * D C B A 
# E D C B A 
