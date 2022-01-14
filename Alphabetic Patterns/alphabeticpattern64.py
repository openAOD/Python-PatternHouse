
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())
counter = n
for i in range(0, n):
    for k in range(0,n-counter):
        print("*",end=" ")
    for j in range(0, n-i):
        print(alpha[counter-1], end=" ")
        
    counter-=1
    print()
    
# Enter the no of rows: 
# 5
# E E E E E 
# * D D D D 
# * * C C C 
# * * * B B 
# * * * * A 
