
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())
for i in range(0, n):
    for k in range(0,n-i-1):
        print("*",end=" ")
    for j in range(0, i+1):
        print(alpha[i], end=" ")
    print()
    
# Enter the no of rows: 
# 5
# * * * * A 
# * * * B B 
# * * C C C 
# * D D D D 
# E E E E E 
